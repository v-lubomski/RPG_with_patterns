"""Классы врагов + фабрика."""

from abc import ABC, abstractmethod
from random import randint


class Enemy:
    type = None
    health = 0
    max_attack = 0
    min_attack = 0
    name = None

    def attack(self, hero) -> int:
        if self.type == hero.type and randint(0, 100) > 90:
            print("Похоже на вмешательство Небес! Неведомым каким-то чудом"
                  " удар врага был заблокирован тобой!")
            return 0
        attack = randint(self.min_attack, self.max_attack)
        return attack


class WarriorEnemy(Enemy):
    type = 'melee'
    name = 'огр'

    def __init__(self):
        self.max_attack = randint(30, 60)
        self.min_attack = int(self.max_attack * 0.7)
        self.health = randint(30, 300)


class ArcherEnemy(Enemy):
    type = 'distant'
    name = 'гоблин-лучник'

    def __init__(self):
        self.max_attack = randint(30, 60)
        self.min_attack = int(self.max_attack * 0.7)
        self.health = randint(30, 300)


class MagicianEnemy(Enemy):
    type = 'magician'
    name = 'чернокнижник'

    def __init__(self):
        self.max_attack = randint(30, 60)
        self.min_attack = int(self.max_attack * 0.7)
        self.health = randint(30, 300)


class EnemyCreator(ABC):
    @abstractmethod
    def create_enemy(self):
        pass


class WarriorEnemyCreator(EnemyCreator):
    def create_enemy(self) -> WarriorEnemy:
        return WarriorEnemy()


class ArcherEnemyCreator(EnemyCreator):
    def create_enemy(self) -> ArcherEnemy:
        return ArcherEnemy()


class MagicianEnemyCreator(EnemyCreator):
    def create_enemy(self) -> MagicianEnemy:
        return MagicianEnemy()
