def mine_filler(n, m, mine_index_list):
    playground = [["#" for j in range(m)] for i in range(n)]

    for loc in mine_index_list:
        playground[loc[0]-1][loc[1]-1] = "*"

    return playground

def show_matrix(matrix):
    for row in matrix:
        str_row = ""
        for col in row:
            str_row += col + " "
        print(str_row)

def calculate_mine_number(n, m, playground):
    for i in range(n):
        for j in range(m):
            if playground[i][j] == "#":

                sum_stars = 0

                try:
                    if playground[i][j-1] == "*" and not j == 0: sum_stars += 1
                except: pass

                try:
                    if playground[i][j+1] == "*" : sum_stars += 1
                except: pass

                try:
                    if playground[i-1][j] == "*" and not i == 0: sum_stars += 1
                except: pass
                
                try:
                    if playground[i+1][j] == "*" : sum_stars += 1
                except: pass

                try:
                    if playground[i-1][j-1] == "*" and not i == 0 and not j == 0 : sum_stars += 1
                except: pass

                try:
                    if playground[i-1][j+1] == "*" and not i == 0: sum_stars += 1
                except: pass

                try:
                    if playground[i+1][j-1] == "*" and not j == 0: sum_stars += 1
                except: pass

                try:
                    if playground[i+1][j+1] == "*" : sum_stars += 1
                except: pass

                playground[i][j] = str(sum_stars)

    show_matrix(playground)
                    

n, m = map(int, input().split())
k_numbers = int(input())

mine_index_list = []
for i in range(k_numbers):
    row, col = map(int, input().split())
    mine_index_list.append([row, col])

playground = mine_filler(n, m, mine_index_list)


calculate_mine_number(n, m, playground)
