import pygame
img = pygame.image.load('in.png')
size = img.get_rect().size
pic_string = pygame.image.tostring(img, 'RGB')
img2 = pygame.image.fromstring(pic_string, size, 'RGB')
pygame.image.save(img2, 'out.png')