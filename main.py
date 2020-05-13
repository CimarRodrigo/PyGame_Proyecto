import pygame
import Colors
from Invader import Invader
from Player import Player
from Window import Window

pygame.init()

player = Player(pos_x=700, pos_y=300, width=0, height=0, vel=5)
inv_1 = Invader(20, 30)
inv_2 = Invader(100, 50)

window_size = Window.window_size()
main_window = Window.main_window()

pygame.display.set_caption("Project")

running_game = True

while running_game:
    pygame.time.delay(5)
    main_window.fill(Colors.black)
    Window.cargar_image(main_window)
    player.cargar_img(main_window)
    inv_1.cargar_img(main_window)
    inv_2.cargar_img(main_window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
            break
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.pos_x > 650:
        player.pos_x -= player.vel

    if keys[pygame.K_RIGHT] and player.pos_x < 750 - player.width:
        player.pos_x += player.vel

    if keys[pygame.K_UP] and player.pos_y > 40:
        player.pos_y -= player.vel

    if keys[pygame.K_DOWN] and player.pos_y < 600 - player.height:
        player.pos_y += player.vel

    inv_1.draw(main_window)
    inv_2.draw(main_window)
    inv_2.move_in_y()
    inv_1.move_in_y()
    inv_1.move_in_x(main_window)
    inv_2.move_in_x(main_window)

    pygame.draw.rect(main_window, Colors.black, (player.pos_x, player.pos_y, player.width, player.height))

    pygame.display.update()

pygame.quit()
