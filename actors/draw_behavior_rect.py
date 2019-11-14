import pygame


class DrawBehaviorRect:

    def draw(self, sc, color, rect):
        pygame.draw.rect(sc, color, rect)
