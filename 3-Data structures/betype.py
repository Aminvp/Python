string = input()

back_space = "="

while True:
    try:
        index_back_space = string.index(back_space)
        string = string[:index_back_space-1] + string[index_back_space+1:]
    except ValueError:
        break

print(string)
