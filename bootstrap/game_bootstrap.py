import pygame

from actors.draw_behavior_rect import DrawBehaviorRect
from actors.hero import Hero
from actors.move_behavior_hero import MoveBehaviorHero
from helpers.color import Colors
from scenes.first_level import FirstLevel


class GameBootstrap:

    def __init__(self, fps, w, h):
        self.fps = fps
        self.w = w
        self.h = h
        self.clock = pygame.time.Clock()
        self.sc = pygame.display.set_mode((w, h))
        self.hero = Hero(pygame.Rect(0, 380, 20, 20), DrawBehaviorRect(), MoveBehaviorHero())
        self.levels = self.__construct_levels()

    def __clear_screen(self):
        self.sc.fill(Colors.WHITE)

    def __construct_levels(self):
        return [
            FirstLevel(self.hero)
        ]

    def __draw_scene(self):
        self.levels[0].draw(self.sc)

    def __update(self, keys):
        res = self.levels[0].update(keys)
        if res is None:
            pass
        elif res is True:
            print('level passed increase')
        elif res is False:
            print('Game over')
            exit()

    def play_game(self):
        while 1:
            self.__clear_screen()
            self.__draw_scene()
            pygame.display.update()

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()

            keys = pygame.key.get_pressed()
            res = self.__update(keys)


            self.clock.tick(self.fps)
            pygame.display.update()
