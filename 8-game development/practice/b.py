dx, dy = map(int, input().split())
t = int(input())

import pygame
img = pygame.image.load('sq.png')

white = (255, 255, 255)
screen = pygame.display.set_mode((640, 480))
screen.fill(white)

x, y = 0, 0

for i in range(t):
    screen.fill(white)
    screen.blit(img,(x , y))
    x, y = x + dx, y + dy

pygame.image.save(screen, 'out.png')