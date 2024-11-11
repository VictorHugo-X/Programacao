import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo 2D Simples')

# Cores
white = (255, 255, 255)
black = (0, 0, 0)

# Posições e dimensões do retângulo
rect_x = 100
rect_y = 100
rect_width = 50
rect_height = 50
speed = 5

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura as teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= speed
    if keys[pygame.K_RIGHT]:
        rect_x += speed
    if keys[pygame.K_UP]:
        rect_y -= speed
    if keys[pygame.K_DOWN]:
        rect_y += speed

    # Preenche o fundo
    screen.fill(white)

    # Desenha o retângulo
    pygame.draw.rect(screen, black, (rect_x, rect_y, rect_width, rect_height))

    # Atualiza a tela
    pygame.display.flip()

    # Define a taxa de quadros
    pygame.time.Clock().tick(60)


