import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 255, 255)
RED = (255, 51, 51)

# Game settings
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_RADIUS = 10
FPS = 60
FONT = pygame.font.SysFont("Arial", 32)

# Paddle positions
player_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
ai_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
player_score = 0
ai_score = 0

# Ball settings
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_vx = 5
ball_vy = 5

def draw():
    WIN.fill(BLACK)
    # Draw center net
    for y in range(0, HEIGHT, 30):
        pygame.draw.rect(WIN, WHITE, (WIDTH//2 - 2, y, 4, 18))
    # Draw paddles
    pygame.draw.rect(WIN, BLUE, (20, player_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(WIN, RED, (WIDTH - 20 - PADDLE_WIDTH, ai_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    # Draw ball
    pygame.draw.circle(WIN, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)
    # Draw score
    WIN.blit(FONT.render(str(player_score), True, WHITE), (WIDTH//4, 20))
    WIN.blit(FONT.render(str(ai_score), True, WHITE), (WIDTH*3//4, 20))
    pygame.display.update()

def reset_ball(direction):
    global ball_x, ball_y, ball_vx, ball_vy
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_vx = 5 * direction
    ball_vy = 5 if direction == 1 else -5

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player paddle follows mouse
    mouse_y = pygame.mouse.get_pos()[1]
    player_y = mouse_y - PADDLE_HEIGHT // 2
    player_y = max(0, min(HEIGHT - PADDLE_HEIGHT, player_y))

    # AI paddle simple follow logic
    if ai_y + PADDLE_HEIGHT // 2 < ball_y - 10:
        ai_y += 5
    elif ai_y + PADDLE_HEIGHT // 2 > ball_y + 10:
        ai_y -= 5
    ai_y = max(0, min(HEIGHT - PADDLE_HEIGHT, ai_y))

    # Move ball
    ball_x += ball_vx
    ball_y += ball_vy

    # Top and bottom collision
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
        ball_vy *= -1

    # Paddle collision (player)
    if (ball_x - BALL_RADIUS <= 20 + PADDLE_WIDTH and
        player_y < ball_y < player_y + PADDLE_HEIGHT):
        ball_vx *= -1
        ball_x = 20 + PADDLE_WIDTH + BALL_RADIUS

    # Paddle collision (AI)
    if (ball_x + BALL_RADIUS >= WIDTH - 20 - PADDLE_WIDTH and
        ai_y < ball_y < ai_y + PADDLE_HEIGHT):
        ball_vx *= -1
        ball_x = WIDTH - 20 - PADDLE_WIDTH - BALL_RADIUS

    # Left/right wall (score)
    if ball_x < 0:
        ai_score += 1
        reset_ball(direction=1)
    if ball_x > WIDTH:
        player_score += 1
        reset_ball(direction=-1)

    draw()

pygame.quit()
sys.exit()