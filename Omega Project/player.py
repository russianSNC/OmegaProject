import random

class Player:
    def __init__(self, life, maxLife, ):
        self._life = 25
        self._lifeMax = 25

        self._attackMax = 6
        self._attackMin = 3

        self._xp = 0
        self._level = 5
        self._shieldLevel = 2
        self._attackLevel = 3


    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, newLife):
        # Evite que a vida seja maior que lifeMax ou menor que 0
        if isinstance(newLife, int): # russo disse que queria que o sistema de vida fosse em INTEGER
            if newLife > self._lifeMax:
                self._life = lifeMax
            elif newLife < 0:
                self._life = 0
            else:
                self._life = newLife

            return self._life
        
        else:
            raise TypeError("newLife needs to be an int")

    @property
    def attackMax(self):
        return self._attackMax

    @attackMax.setter
    def attackMax(self, newAttackMax):
        if isinstance(newAttackMax, int):
            self._attackMax = newAttackMax
        else:
            raise TypeError("AttackMax needs to be int")

    @property
    def attackMin(self):
        return self._attackMin

    @attackMin.setter
    def attackMin(self, newAttackMin):
        if  instance(newAttackMin, int):
            self._attackMin = newAttackMin
        else:
            raise TypeError("AttackMin needs to be an integer")

    @property
    def xp(self):
        return self._xp
    
    @xp.setter
    def xp(self, newXp):
        if newXp >= 100:
            level += 1




    def checkLevel(self):
        if self._shieldLevel + self._attackLevel < self._level:
            return self._level - (self._shieldLevel + self._attackLevel)
        else:
            return 0

    def attack(self, enemy):
        damage = random.randrange(self._attackMin, self._attackMax + 1) + self._attackLevel - enemy._shieldLevel
        enemy.life -= damage

        return damage
