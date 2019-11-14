class ActorBase:

    def __init__(self, rect, draw_behavior, move_behavior, jump_behavior=None):
        self.rect = rect
        self.move_behavior = move_behavior
        self.draw_behavior = draw_behavior
        self.jump_behavior = jump_behavior

    def colliderect(self, other_actor):
        return self.rect.colliderect(other_actor.rect)

    def collidelist(self, list_of_actors):
        return self.rect.collidelist(list_of_actors)

    def move(self, x=None, y=None):
        self.move_behavior.move(x, y, self)

    def draw(self, *args, **kwargs):
        self.draw_behavior.draw(*args, **kwargs)