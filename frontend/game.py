import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da janela do jogo
SCREEN_WIDTH = 800  # Largura da tela
SCREEN_HEIGHT = 600  # Altura da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Criar a tela
pygame.display.set_caption('Bounce & Block')  # Título da janela do jogo

# Cores
WHITE = (255, 255, 255)  # Cor de fundo da tela
RED = (255, 0, 0)  # Cor da bola
BLUE = (0, 0, 255)  # Cor do retângulo

# Definir o relógio para controle de FPS
clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # Fechar o jogo

    # Preencher o fundo da tela com a cor branca
    screen.fill(WHITE)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar o FPS
    clock.tick(60)  # Atualiza 60 vezes por segundo
