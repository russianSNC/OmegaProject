import random

class Enemy:
    def __init__(self, life, shieldLevel, attackLevel, attackMax, attackMin):
        self._life = life
        self._lifeMax = life
    
        self._shieldLevel = shieldLevel
        self._attackLevel = attackLevel

        self._attackMax = attackMax
        self._attackMin = attackMin

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, newLife):
        # Evite que a vida seja maior que lifeMax ou menor que 0
        if newLife > self._lifeMax:
            self._life = lifeMax
        elif newLife < 0:
            self._life = 0
        else:
            self._life = newLife

        return self._life



    def attack(self, enemy):
        damage = random.randrange(self._attackMin, self._attackMax + 1) + self._attackLevel - enemy._shieldLevel
        enemy.life -= damage

        return damage