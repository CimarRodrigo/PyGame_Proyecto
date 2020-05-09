import pygame
import Colors
from Window import Window

window = Window(window_width=800, window_height=600)


class Invader:
    sw = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

    def draw(self, pygame_window):
        pygame.draw.rect(pygame_window, Colors.white, (self.x, self.y, self.width, self.height))

    # SI USAMOS EL SW COMO ATRIBUTO DE OBJETO CADA UNO FUNCIONARA INDEPENDIENTE

    def move_in_y(self, pygame_window):

        if window.window_height - 30 > self.y and Invader.sw == 0:
            self.y += 2
        else:
            Invader.sw = 1
            self.y -= 2
            if self.y == 30 and Invader.sw == 1:
                Invader.sw = 0

    def move_in_x(self, pygame_window):
        self.x += 10
        self.draw(pygame_window)
    # def update(self):
