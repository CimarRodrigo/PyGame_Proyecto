import pygame


class Window:
    window_width = 800
    window_height = 600
    background = pygame.image.load("images/background.png")

    @classmethod
    def window_size(cls):
        return (cls.window_width, cls.window_height)

    @classmethod
    def main_window(cls):
        return pygame.display.set_mode(cls.window_size())

    @staticmethod
    def cargar_image(window):
        window.blit(Window.background, (0, 0))
