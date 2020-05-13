import pygame


class Player:
    def __init__(self, pos_x, pos_y, width, height, vel):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.vel = vel
        self.imagen = pygame.image.load("images/nave.png")

    def cargar_img(self, pantalla):
        pantalla.blit(self.imagen, (self.pos_x - 50, self.pos_y - 50))
