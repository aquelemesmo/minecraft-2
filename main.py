import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 925
altura = 465

x = 0

y = 0

tela = pygame.display.set_mode((largura, altura))
programIcon = pygame.image.load('image/grama.png')

pygame.display.set_caption('Minecraft 2 | Edição Python')
pygame.display.set_icon(programIcon)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        pygame.draw.circle(tela, (255, 0, 0), (300, 260), 40)
        pygame.draw.line(tela, (19, 255, 0), (390, 0), (390, 600), 10)
    pygame.display.update()