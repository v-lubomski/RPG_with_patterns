"""Классы оружия + фабрика."""

from abc import ABC, abstractmethod
from random import randint


class Weapon:
    """Класс оружия."""

    max_attack = 0
    min_attack = 0
    type = None
    name = None


class Sword(Weapon):
    """Класс оружия ближнего боя."""

    type = 'melee'
    name = 'меч'

    def __init__(self):
        """Создает кастомные характеристики каждому оружию."""
        self.max_attack = randint(30, 60)
        self.min_attack = int(self.max_attack * 0.7)


class Bow(Weapon):
    """Класс оружия дальнего боя."""

    type = 'distant'
    name = 'лук'

    def __init__(self):
        """Создает кастомные характеристики каждому оружию."""
        self.max_attack = randint(30, 60)
        self.min_attack = int(self.max_attack * 0.7)


class MagicianBook(Weapon):
    """Класс магического оружия."""

    type = 'magician'
    name = 'магическая книга'

    def __init__(self):
        """Создает кастомные характеристики каждому оружию."""
        self.max_attack = randint(30, 60)
        self.min_attack = int(self.max_attack * 0.7)


class WeaponCreator(ABC):
    """Оружейная фабрика."""

    @abstractmethod
    def create_weapon(self):
        """Интерфейс создания оружия."""
        pass


class SwordCreator(WeaponCreator):
    """Конкретная фабрика по созданию мечей."""

    def create_weapon(self) -> Weapon:
        """Воплощение интерфейса создания оружия."""
        return Sword()


class BowCreator(WeaponCreator):
    """Конкретная фабрика по созданию луков."""

    def create_weapon(self) -> Weapon:
        """Воплощение интерфейса создания оружия."""
        return Bow()


class MagicianBookCreator(WeaponCreator):
    """Конкретная фабрика по созданию магических книг."""

    def create_weapon(self) -> Weapon:
        """Воплощение интерфейса создания оружия."""
        return MagicianBook()
