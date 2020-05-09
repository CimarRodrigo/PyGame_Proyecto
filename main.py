import pygame
import Colors
from Invader import Invader
from Player import Player
from Window import Window
from pygame.locals import *

pygame.init()

player = Player(pos_x=700, pos_y=300, width=0, height=0, vel=5)
window = Window(window_width=800, window_height=600)
inv_1 = Invader(20, 30)
inv_2 = Invader(60, 50)

window_size = window.window_size()
main_window = window.main_window()

pygame.display.set_caption("Project")

running_game = True

while running_game:
    pygame.time.delay(10)
    main_window.fill(Colors.black)
    player.cargar_img(main_window)
    # pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
            break
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.pos_x > 650:
        player.pos_x -= player.vel

    if keys[pygame.K_RIGHT] and player.pos_x < 750 - player.width:
        player.pos_x += player.vel

    if keys[pygame.K_UP] and player.pos_y > 0:
        player.pos_y -= player.vel

    if keys[pygame.K_DOWN] and player.pos_y < 600 - player.height:
        player.pos_y += player.vel

    inv_1.draw(main_window)
    inv_1.move_in_y(main_window)
    # inv_1.move_in_x(main_window)
    inv_2.draw(main_window)
    inv_2.move_in_y(main_window)

    pygame.draw.rect(main_window, not color.Color, (player.pos_x, player.pos_y, player.width, player.height))

    pygame.display.update()

pygame.quit()
