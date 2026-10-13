import pygame
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Football - Press SPACE to shoot")
clock = pygame.time.Clock()

# Ball
ball_x, ball_y = 400, 500
ball_vx, ball_vy = 0, 0
ball_radius = 20
shooting = False

# Goal
goal = pygame.Rect(WIDTH//2 - 100, 50, 200, 20)

# Keeper
keeper_x = WIDTH//2
keeper_dir = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not shooting:
                # kick towards goal with random angle
                angle = math.radians(90 + (pygame.time.get_ticks() % 40 - 20))
                power = 15
                ball_vx = math.cos(angle) * power
                ball_vy = -math.sin(angle) * power
                shooting = True

    # Move ball
    if shooting:
        ball_x += ball_vx
        ball_y += ball_vy
        ball_vx *= 0.99
        ball_vy *= 0.99
        # friction
        if abs(ball_vx) < 0.1 and abs(ball_vy) < 0.1:
            shooting = False

    # Move keeper left-right
    keeper_x += keeper_dir
    if keeper_x < WIDTH//2 - 90 or keeper_x > WIDTH//2 + 90:
        keeper_dir *= -1

    # Goal check
    if goal.collidepoint(ball_x, ball_y):
        print("GOOOAL!")
        ball_x, ball_y = 400, 500
        ball_vx, ball_vy = 0, 0
        shooting = False

    # Draw
    screen.fill((40, 150, 40))
    pygame.draw.rect(screen, (255,255,255), goal, 2)
    pygame.draw.rect(screen, (255,0,0), (keeper_x-25, 70, 50, 10))
    pygame.draw.circle(screen, (255,255,255), (int(ball_x), int(ball_y)), ball_radius)
    pygame.draw.circle(screen, (0,0,0), (int(ball_x), int(ball_y)), ball_radius, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()