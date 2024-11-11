import pygame
import sys

# Inicializa o Pygame
pygame.init()

pygame.mixer_music.set_volume (0.9)
musica_de_fundo = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

barulho_colisao=pygame.mixer.Sound("music.mp3")
barulho_colisao.set_volume(0.9)

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo de Luta')

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Configurações dos lutadores
player1_pos = [100, 500]
player2_pos = [600, 500]
player_size = 50
speed = 5

# Variável de ataque
player1_attacking = True
player2_attacking = False

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura as teclas pressionadas
    keys = pygame.key.get_pressed()

    # Movimentação do Jogador 1
    if keys[pygame.K_a]:
        player1_pos[0] -= speed
    if keys[pygame.K_d]:
        player1_pos[0] += speed
    if keys[pygame.K_w]:
        player1_attacking = True
    else:
        player1_attacking = False

    # Movimentação do Jogador 2
    if keys[pygame.K_LEFT]:
        player2_pos[0] -= speed
    if keys[pygame.K_RIGHT]:
        player2_pos[0] += speed
    if keys[pygame.K_UP]:
        player2_attacking = True
    else:
        player2_attacking = False

    # Preenche o fundo
    screen.fill(white)

    # Desenha os lutadores
    pygame.draw.rect(screen, blue, (player1_pos[0], player1_pos[1], player_size, player_size))
    pygame.draw.rect(screen, red, (player2_pos[0], player2_pos[1], player_size, player_size))

    # Verifica ataques
    if player1_attacking:
        pygame.draw.rect(screen, black, (player1_pos[0] + player_size, player1_pos[1] + 10, 30, 10))
    if player2_attacking:
        pygame.draw.rect(screen, black, (player2_pos[0] - 30, player2_pos[1] + 10, 30, 10))



    # Atualiza a tela
    pygame.display.flip()

    # Define a taxa de quadros
    pygame.time.Clock().tick(60)