import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Definição das dimensões da tela
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Configuração da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Função para desenhar a cobra
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, BLACK, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Função para gerar comida em uma posição aleatória
def generate_food():
    x = random.randint(0, WIDTH - CELL_SIZE)
    y = random.randint(0, HEIGHT - CELL_SIZE)
    return x // CELL_SIZE * CELL_SIZE, y // CELL_SIZE * CELL_SIZE

# Movimentos
UP = (0, -CELL_SIZE)
DOWN = (0, CELL_SIZE)
LEFT = (-CELL_SIZE, 0)
RIGHT = (CELL_SIZE, 0)

# Função principal
def main():
    snake = [(WIDTH / 2, HEIGHT / 2)]
    snake_direction = RIGHT
    food = generate_food()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_direction = UP
                elif event.key == pygame.K_DOWN:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT:
                    snake_direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    snake_direction = RIGHT
                elif event.key == pygame.K_a:
                    snake_direction = LEFT
                elif event.key == pygame.K_s:
                    snake_direction = DOWN
                elif event.key == pygame.K_d:
                    snake_direction = RIGHT
                elif event.key == pygame.K_w:
                    snake_direction = UP

        # Movimento da cobra
        x, y = snake[0]
        x += snake_direction[0]
        y += snake_direction[1]
        snake.insert(0, (x, y))

        # Verificação de colisão com a parede
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            pygame.quit()
            quit()

        # Verificação de colisão com a própria cobra
        if snake[0] in snake[1:]:
            pygame.quit()
            quit()

        # Verificação de colisão com a comida
        if snake[0] == food:
            food = generate_food()
        else:
            snake.pop()

        # Limpar a tela
        screen.fill(WHITE)

        # Desenhar a comida
        pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

        # Desenhar a cobra
        draw_snake(snake)

        # Atualizar a tela
        pygame.display.update()

        # Configurar a taxa de quadros por segundo (FPS)
        clock.tick(10)

# Executar o jogo
if __name__ == "__main__":
    main()
