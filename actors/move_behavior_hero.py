class MoveBehaviorHero:

    def move(self, x, y, actor):
        if x:
            actor.rect.x = x
        if y:
            actor.rect.y = y