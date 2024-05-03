import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição de constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
SNAKE_SPEED = 10

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Classe para a Cobra
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*BLOCK_SIZE)) % SCREEN_WIDTH), (cur[1] + (y*BLOCK_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = UP
                elif event.key == pygame.K_DOWN:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = RIGHT
                elif event.key == pygame.K_a:
                    self.direction = LEFT
                elif event.key == pygame.K_s:
                    self.direction = DOWN
                elif event.key == pygame.K_d:
                    self.direction = RIGHT
                elif event.key == pygame.K_w:
                    self.direction = UP

# Classe para a Comida
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, SCREEN_WIDTH//BLOCK_SIZE - 1) * BLOCK_SIZE,
                         random.randint(0, SCREEN_HEIGHT//BLOCK_SIZE - 1) * BLOCK_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)

# Direções
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
    # Inicialização da tela
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')

    # Inicialização dos objetos
    snake = Snake()
    food = Food()

    # Relógio para controle de tempo
    clock = pygame.time.Clock()

    # Pontuação
    score = 0
    font = pygame.font.SysFont(None, 30)

    while True:
        # Manipulação de eventos
        snake.handle_keys()

        # Atualização da cobra
        snake.move()

        # Verificação de colisão com a comida
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()

        # Desenho na tela
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)

        # Desenho da pontuação
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

        # Atualização da tela
        pygame.display.update()

        # Limitação de taxa de quadros por segundo
        clock.tick(SNAKE_SPEED)

if __name__ == "__main__":
    main()
