import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))

white = (255, 255, 255)
screen.fill(white)

color = (0, 0, 0)
font = 1


while True:
    pygame.event.pump()

    x = list(input().split())
    if x[0] == 'change' and x[1] == 'size':
        font = int(x[2])
        pygame.display.update()
    if x[0] == 'change' and x[1] == 'color':
        color = (int(x[2]), int(x[3]), int(x[4]))
        pygame.display.update()
    if x[0] == 'draw' and x[1] == 'line':
        y = (int(x[2]), int(x[3]))
        z = (int(x[4]), int(x[5]))
        pygame.draw.line(screen, color, y, z, font)
        pygame.display.update()
    if x[0] == 'draw' and x[1] == 'circle':
        o = (int(x[2]), int(x[3]))
        r = int(x[4])
        pygame.draw.circle(screen, color, o, r, font)
        pygame.display.update()
    if x[0] == 'draw' and x[1] == 'polygon':
        len = len(x)
        listA = [int(y) for y in x[2:len:2]]
        listB = [int(z) for z in x[3:len:2]]
        ls = [(int(y), int(z)) for y, z in zip(listA, listB)] 
        print(ls)
        pygame.draw.polygon(screen, color, ls, font)
        pygame.display.update()
    if x[0] == 'end' and x[1] == 'drawing':
        pygame.image.save(screen, 'draw.png')
        break

   


