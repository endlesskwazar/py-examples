import pygame

from actors.draw_behavior_rect import DrawBehaviorRect
from actors.dump_enemy import DumpEnemy
from helpers.color import Colors
from scenes.scene_base import SceneBase


class FirstLevel(SceneBase):

    def __init__(self, hero):
        super().__init__(hero)
        self.enemies = [
            DumpEnemy(pygame.Rect(140, 380, 20, 20), DrawBehaviorRect(), None),
            DumpEnemy(pygame.Rect(220, 380, 20, 20), DrawBehaviorRect(), None),
            DumpEnemy(pygame.Rect(350, 380, 20, 20), DrawBehaviorRect(), None)
        ]
        self.jumped = False

    def draw(self, sc):
        self.hero.draw(sc, Colors.GREEN, self.hero.rect)
        for enemy in self.enemies:
            enemy.draw(sc, Colors.PINK, enemy.rect)

    def update(self, keys):
        if self.hero.collidelist(self.enemies) is not -1:
            return False

        if keys[pygame.K_LEFT]:
            self.hero.move(x=self.hero.rect.x - 3)
        if keys[pygame.K_RIGHT]:
            self.hero.move(x=self.hero.rect.x + 3)
        if keys[pygame.K_SPACE] and not self.jumped:
            self.jumped = True
            self.hero.move(y=self.hero.rect.y - 40)
        elif self.jumped and self.hero.rect.y != 380:
            self.hero.move(y=self.hero.rect.y + 1)
        else:
            self.jumped = False

        print(self.hero.rect.x)

        if self.hero.rect.x > 680:
            print('level complete')
            return True