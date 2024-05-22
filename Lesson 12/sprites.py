import pygame
import random


class Block(pygame.sprite.Sprite):
    pass


class Car():
    def __init__(self, kerekmeret, color):
        self.kerekmeret = kerekmeret
        self.color = color

    def nulla_km(self):
        return "A km ora allasa 0 lett."


car1 = Car(19, "black")

print(car1.color)
print(car1.kerekmeret)

print(car1.nulla_km())


class MilitaryCar(Car):
    def __init__(self, kerekmeret, color, bulletsize):
        super().__init__(kerekmeret, color)
        self.bulletsize = bulletsize

    def loves(self):
        return "Loves megtortent"


militaryCar1 = MilitaryCar(19, "zold", 88)


print(militaryCar1.color)
print(militaryCar1.kerekmeret)
print(militaryCar1.bulletsize)

print(militaryCar1.loves())