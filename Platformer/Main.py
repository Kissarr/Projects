import pygame
import engine
import sys

# Значения
screen_size = (700, 600)
dark_gray = (50, 50, 50)
platform_color = (19, 197, 207)
player_x = 600
player_y = 300
player_speed = 0
player_acceleration = 0.15
FPS = 60
player_w = 45
player_h = 51
score = 0
lives = 3
shrift = 24
player_derection = "right"
player_state = "idle"

player_animations = {
    "idle": engine.Anination([
        pygame.image.load("sprite_00.png"),
        pygame.image.load("sprite_01.png"),
        pygame.image.load("sprite_02.png"),
        pygame.image.load("sprite_03.png"),

    ]),
    "walking": engine.Anination([
        pygame.image.load("sprite_04.png"),
        pygame.image.load("sprite_05.png"),
        pygame.image.load("sprite_06.png"),
        pygame.image.load("sprite_07.png"),
        pygame.image.load("sprite_08.png"),
        pygame.image.load("sprite_09.png")
    ])}


# Функции


def drawText(t, x, y, s):
    text = font.render(t, True, s, dark_gray)
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)


# Запуск
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 24)
# GameStatus
game_state = "playing"
# Изображения
player_images = pygame.image.load("sprite_03.png")
coin_images = pygame.image.load("star_1.png")
coin_animation = engine.Anination([
    pygame.image.load("star_1.png"), pygame.image.load("star_2.png"),
    pygame.image.load("star_3.png"), pygame.image.load("star_4.png"),
    pygame.image.load("star_5.png"),
])
# walkRight = [pygame.image.load("sprite_04.png"), pygame.image.load("sprite_05.png"),
# pygame.image.load("sprite_06.png"), pygame.image.load("sprite_07.png"),
# pygame.image.load("sprite_08.png"), pygame.image.load("sprite_09.png"), ]
enemy_images = pygame.image.load("spiky.png")
heart_images = pygame.image.load("heart.png")
# Платформы
platform = [pygame.Rect(100, 300, 400, 50),
            pygame.Rect(100, 250, 50, 50),
            pygame.Rect(450, 250, 50, 50),
            pygame.Rect(0, 425, 300, 50),
            pygame.Rect(450, 450, 50, 100),
            pygame.Rect(550, 400, 300, 50),
            pygame.Rect(250, 100, 400, 50),
            pygame.Rect(450, 550, 400, 50),
            pygame.Rect(0, 100, 100, 50),
            pygame.Rect(0, 550, 400, 50),
            pygame.Rect(-50, 0, 50, 600),
            pygame.Rect(700, 0, 50, 600),
            pygame.Rect(-50, 0, 50, 600),
            ]
# Деньги
coins = [pygame.Rect(110, 200, 23, 23),
         pygame.Rect(250, 250, 23, 23),
         pygame.Rect(500, 61, 36, 35),
         pygame.Rect(550, 511, 36, 35),
         pygame.Rect(50, 50, 36, 35),
         pygame.Rect(100, 511, 36, 35)]
# Враги
enemy = [pygame.Rect(160, 261, 36, 35),
         pygame.Rect(425, 61, 36, 35),
         pygame.Rect(650, 511, 36, 35),
         pygame.Rect(410, 650, 36, 35),
         pygame.Rect(60, 511, 36, 35)]
# Основа
runnung = True
while runnung:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnung = False
    if game_state == "playing":
        # Ввод с клавиатуры
        new_player_x = player_x
        new_player_y = player_y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            new_player_x -= 2  # Лево
            player_derection = "left"
            player_state = "walking"
        if keys[pygame.K_d]:
            new_player_x += 2  # Право
            player_derection = "right"
            player_state = "walking"
        if not keys[pygame.K_d] and not keys[pygame.K_a]:
            player_state = "idle"
        if keys[pygame.K_w] and player_on_ground:
            player_speed = -7  # Верх

    if game_state == "playing":
        coin_animation.update()
        player_animations[player_state].update()
        # Коллизия
        new_player_rect = pygame.Rect(new_player_x, player_y, player_w, player_h)
        x_collision = False

        for p in platform:
            if p.colliderect(new_player_rect):
                x_collision = True
                break

        if x_collision == False:
            player_x = new_player_x

        # Вертикальное передвижение
        player_speed += player_acceleration
        new_player_y += player_speed

        new_player_rect = pygame.Rect(player_x, new_player_y, player_w, player_h)
        y_collision = False
        player_on_ground = False

        for p in platform:
            if p.colliderect(new_player_rect):
                y_collision = True
                player_speed = 0
                # Сравнение уровня по у платформы и персонажа
                if p[1] > new_player_y:
                    # player_y = p[1] + player_h
                    player_on_ground = True
                break

        if y_collision == False:
            player_y = new_player_y
        player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
        for c in coins:
            if c.colliderect(player_rect):
                coins.remove(c)
                score += 1
                if score >= 6:
                    game_state = "Win"

        for e in enemy:
            if e.colliderect(player_rect):
                lives -= 1
                player_x = 600
                player_y = 300
                player_speed = 0
                if lives <= 0:
                    game_state = "Lose"
    screen.fill(dark_gray)
    if game_state == "playing":

        # Рисовка (Персонаж)
        if player_derection == "right":
            # screen.blit(player_images, (player_x, player_y))
            player_animations[player_state].draw(screen, player_x, player_y, False, False)
        elif player_derection == "left":
            # screen.blit(pygame.transform.flip(player_images, True, False), (player_x, player_y))
            player_animations[player_state].draw(screen, player_x, player_y, True, False)

        # Рисовка
        for p in platform:
            pygame.draw.rect(screen, platform_color, p)
        # Деньги
        for c in coins:
            # screen.blit(coin_images, (c[0], c[1]))
            coin_animation.draw(screen, c[0], c[1], False, False)
        # Враги
        for e in enemy:
            screen.blit(enemy_images, (e[0], e[1]))

        # Display
        screen.blit(coin_images, (10, 10))
        drawText(str(score), 50, 10, platform_color)
        # score_text = font.render("Score: " + str(score), True, platform_color, dark_gray)
        # score_text_rect = score_text.get_rect()
        # score_text_rect.topleft = (10,10)
        # screen.blit(score_text, score_text_rect)

        for l in range(lives):
            screen.blit(heart_images, (200 + (l * 35), 10))

    if game_state == "Win":
        font = pygame.font.Font(pygame.font.get_default_font(), 99)
        drawText("You WIN", 150, 150, (0, 255, 0))




    if game_state == "Lose":
        font = pygame.font.Font(pygame.font.get_default_font(), 99)
        drawText("You DIE", 150, 150, (255, 0, 0))


    pygame.display.flip()
    clock.tick(FPS)

# Выход
pygame.quit()
