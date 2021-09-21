import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

fundo = pygame.mixer.music.load('music/Minecraft Volume Alpha - 18 - Sweden.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.7)

efeito_sonoro = pygame.mixer.Sound('music/Efeito Sonoro-(Soco).mp3')
efeito_sonoro.set_volume(0.01)


largura = 925
altura = 465
fonte = pygame.font.SysFont('blox', 40, True, True)
x = int(largura/2)
y = int(altura/2)

pontos = 0
tela = pygame.display.set_mode((largura, altura))
programIcon = pygame.image.load('imagem/grama.png')

pygame.display.set_caption('Minecraft 2')
pygame.display.set_icon(programIcon)
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[K_a]:
            x = x - 20
        if pygame.key.get_pressed()[K_d]:
            x = x + 20
        if pygame.key.get_pressed()[K_w]:
            y = y - 20
        if pygame.key.get_pressed()[K_s]:
            y = y + 20
        boneco = pygame.draw.rect(tela, (255, 0, 0), (x,y, 40, 50))
        boneco2 = pygame.draw.rect(tela, ('BLUE'), (200, 300, 40, 40))

        if boneco.colliderect(boneco2):
            pontos = pontos + 1
            efeito_sonoro.play()

    tela.blit(texto_formatado, (650, 20))

    pygame.display.update()
