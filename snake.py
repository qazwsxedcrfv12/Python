import pygame
import random
pygame.init()


white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

win = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Snake Game")

exit_game = False
game_over = False
bg = pygame.image.load('bg.jpg')
win.blit(bg, (0, 0))
x = 20
y = 40
width = 20
height = 15
vel = 3
vx = 0
vy = 0
score = 0
fps = 50
clock = pygame.time.Clock()

fod_x = random.randint(0, 400)
fod_y = random.randint(0, 300)
font = pygame.font.SysFont(None, 55)


def text_1(text, color, a, b):
    screen_text = font.render(text, True, color)
    win.blit(screen_text, [a, b])


def redraw():
    win.blit(bg, (0, 0))
    pygame.display.update()


while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vx = 3
                vy = 0
            if event.key == pygame.K_LEFT:
                vx = -3
                vy = 0
            if event.key == pygame.K_UP:
                vy = -3
                vx = 0
            if event.key == pygame.K_DOWN:
                vy = 3
                vx = 0
    x += vx
    y += vy
    if abs(x-fod_x) < 6 and abs(y-fod_y) < 6:
        score += 1
        print(f"Score is {score}")
        fod_x = random.randint(0, 600)
        fod_y = random.randint(0, 500)

    redraw()
    text_1("Score: " + str(score*10), black, 1, 1)
    pygame.draw.rect(win, red, (fod_x, fod_y, width, height))
    pygame.draw.rect(win, black, (x, y, width, height))
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
