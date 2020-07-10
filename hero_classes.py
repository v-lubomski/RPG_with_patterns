"""Классы героя + фабрика."""

from abc import ABC, abstractmethod
from weapons_classes import Sword
from random import randint


class Hero:
    """Класс героя."""

    type = None
    health = 100
    defeated_monsters = 0
    arrows = 0
    weapons = {"меч": Sword(), "лук": None, "магическая книга": None}

    def show_my_weapons(self) -> list:
        """Выводит список оружия, которое в наличии у героя."""
        # Наполнение вариантов оружия, предлагаемых для выбора игроку
        existing_weapons = []
        for weapon in self.weapons:
            if self.weapons[weapon]:
                existing_weapons.append(weapon)
        return existing_weapons

    def attack(self) -> int:
        """Возвращает размер урона, который нанесёт герой."""
        existing_weapons = self.show_my_weapons()

        def choose_weapon() -> str:
            """Функция, предоставляющая возможность выбрать оружие для удара."""
            # Цикл проверки, что введённый игроком вариант существует
            answer = None
            while answer not in existing_weapons:
                print('Выберите оружие для атаки:')
                # Выводим существующее у игрока оружие
                for weapon in existing_weapons:
                    # Если это лук - выводим количество стрел
                    if weapon == 'лук':
                        print(f'{existing_weapons.index(weapon) + 1} -'
                              f'{weapon} (количество стрел: {self.arrows})')
                    else:
                        print(f'{existing_weapons.index(weapon) + 1}'
                              f'- {weapon}')

                # Сама проверка
                try:
                    answer = existing_weapons[int(input()) - 1]
                except (IndexError, TypeError, ValueError):
                    print('Вы ввели неверное значение. Попробуйте ещё раз.\n')
            return answer

        # Берём выбранное оружие в руки
        current_weapon = self.weapons[choose_weapon()]
        min_attack = current_weapon.min_attack
        max_attack = current_weapon.max_attack

        # Если типы оружия и героя совпадают -
        # увеличиваем максимальный предел случайного показателя атаки
        if self.type == current_weapon.type:
            max_attack = int(max_attack * 1.5)
        hit_power = randint(min_attack, max_attack)

        if current_weapon.name == 'лук' and self.arrows <= 0:
            print("Так как без стрел выстрелить из лука не получится, "
                  "вы бьёте противника луком плашмя")
            return 1
        if current_weapon.name == 'лук' and self.arrows > 0:
            self.arrows -= 1
        return hit_power


class WarriorHero(Hero):
    """Подкласс героя-воина."""

    type = 'melee'


class ArcherHero(Hero):
    """Подкласс героя-лучника."""

    type = 'distant'


class MagicianHero(Hero):
    """Подкласс героя-мага."""

    type = 'magician'


class HeroCreator(ABC):
    """Абстрактная фабрика."""

    @abstractmethod
    def create_hero(self):
        """Интерфейс для функции создания героя."""
        pass


class WarriorHeroCreator(HeroCreator):
    """Конкретная фабрика, производящая героев-воинов."""

    def create_hero(self) -> Hero:
        """Метод создания героя-воина."""
        return WarriorHero()


class ArcherHeroCreator(HeroCreator):
    """Конкретная фабрика, производящая героев-лучников."""

    def create_hero(self) -> Hero:
        """Метод создания героя-лучника."""
        return ArcherHero()


class MagicianHeroCreator(HeroCreator):
    """Конкретная фабрика, производящая героев-магов."""

    def create_hero(self) -> Hero:
        """Метод создания героя-мага."""
        return MagicianHero()
