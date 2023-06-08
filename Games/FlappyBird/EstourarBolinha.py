import pygame

# Inicializar o pygame
pygame.init()

# Definir as dimensões da tela
screen_width = 800
screen_height = 600

# Definir as cores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Criar a tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Meu Jogo")

# Definir a fonte para as instruções e o botão
font = pygame.font.Font(None, 30)

# Definir as instruções
instructions = ["Use as setas para se mover", "Pressione a barra de espaço para atirar"]

# Definir o botão "Iniciar"
button_width = 100
button_height = 50
button_x = screen_width / 2 - button_width / 2
button_y = screen_height - 150

# Loop principal
running = True
while running:
    # Lidar com eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                # O botão "Iniciar" foi pressionado
                running = False

    # Preencher a tela com a cor preta
    screen.fill(black)

    # Desenhar as instruções na tela
    for i, text in enumerate(instructions):
        text_surface = font.render(text, True, white)
        text_rect = text_surface.get_rect()
        text_rect.center = (screen_width / 2, (i + 2) * 50)
        screen.blit(text_surface, text_rect)

    # Desenhar o botão "Iniciar" na tela
    pygame.draw.rect(screen, green, (button_x, button_y, button_width, button_height))
    button_text = font.render("Iniciar", True, black)
    button_text_rect = button_text.get_rect()
    button_text_rect.center = (screen_width / 2, button_y + button_height / 2)
    screen.blit(button_text, button_text_rect)

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o pygame
pygame.quit()

import pygame
import random

pygame.init()

# Defina as dimensões da janela do jogo
window_width = 600
window_height = 400
game_display = pygame.display.set_mode((window_width, window_height))

class Ball:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))

    def draw(self):
        game_display.blit(self.image, (self.x - self.image.get_width() // 2,
                                       self.y - self.image.get_height() // 2))


def generate_ball():
    x = random.randint(50, window_width - 50)
    y = random.randint(50, window_height - 50)
    image_path = "D:\Repositorio\Python\FlappyBird\imgs\ladrao.png"  # Substitua pelo caminho para a sua imagem de bola
    return Ball(x, y, image_path)

# Defina o intervalo em segundos entre cada geração de bola
interval = 1

# Defina o tempo em que a próxima bola deve ser gerada
next_ball_time = pygame.time.get_ticks() + interval * 1000

balls = []
score = 0 # Adiciona o contador de pontos
acumulos = 0
intervalo = 1000

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    game_display.fill((255, 255, 255))

    current_time = pygame.time.get_ticks()

    # Exibe mensagem de "Game Over"
    if acumulos >= 10:
        font = pygame.font.Font(None, 52)
        text = font.render(f"O amor venceu e você PERDEU", True, (255, 0, 0))
        font = pygame.font.Font(None, 36)
        text2 = font.render(f"Pontuação: {score}", True, (0, 0, 0))
        text3 = font.render("Se um Lula F*de Um Pais Imagina 10", True, (0, 0, 0))
        game_display.blit(text2, (10, 10))
        game_display.blit(text, (
            window_width // 2 - text.get_width() // 2, window_height // 2 - text.get_height() // 2))
        game_display.blit(text3, (
            window_width // 2 - text.get_width() // 2, window_height // 2 - text.get_height() // 2 + 50))
        pygame.display.update()
        pygame.time.delay(1000)

    # Se for hora de gerar a próxima bola
    if current_time >= next_ball_time:
        balls.append(generate_ball())
        next_ball_time = current_time + interval * intervalo
        acumulos += 1

    for ball in balls:
        ball.draw()

        # Verifica se o botão esquerdo do mouse foi pressionado
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()

            # Verifica se o clique do mouse ocorreu dentro da área da bola
            if ball.x - ball.image.get_width() <= mouse_pos[0] <= ball.x + ball.image.get_width() \
            and ball.y - ball.image.get_width() <= mouse_pos[1] <= ball.y + ball.image.get_width():
                balls.remove(ball)
                score += 1 # Incrementa o contador de pontos
                acumulos -= 1
                intervalo -= 10


                # Mostra o contador de pontos na tela
    font = pygame.font.Font(None, 36)
    text = font.render(f"Pontuação: {score}", True, (0, 0, 0))
    game_display.blit(text, (10, 10))

    pygame.display.update()