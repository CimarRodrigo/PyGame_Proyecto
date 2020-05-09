import pygame
import Colors


class Window:

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

    def window_size(self):
        return (self.window_width, self.window_height)

    def main_window(self):
        return pygame.display.set_mode(self.window_size())
