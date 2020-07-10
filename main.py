"""Основной файл игры с механикой и логикой."""

from hero_classes import WarriorHeroCreator, ArcherHeroCreator, \
    MagicianHeroCreator, Hero
from enemies_classes import WarriorEnemyCreator, ArcherEnemyCreator,\
    MagicianEnemyCreator, Enemy
from weapons_classes import SwordCreator, BowCreator, MagicianBookCreator

from random import randint, choice
from time import sleep
import pickle

from colorama import Fore, Style


saved_games_flag = 0


def status() -> None:
    """Выводит информацию о герое."""
    sleep(1)
    print(Fore.RED + '='*20)
    print(Fore.YELLOW + f'Тип: {hero.type}, здоровье: {hero.health}, '
          f'убитых монстров: {hero.defeated_monsters}, стрел: {hero.arrows}')
    print(Fore.YELLOW + f'Оружие: {", ".join(hero.show_my_weapons())}')
    print(Fore.RED + '='*20)
    print(Style.RESET_ALL)
    sleep(1)


def choice_of_hero() -> Hero:
    """Функция помогает выбрать героя на старте."""
    choices = {'1': WarriorHeroCreator, '2': ArcherHeroCreator,
               '3': MagicianHeroCreator}
    answer = None
    while answer not in ('1', '2', '3'):
        answer = input('Выберите класс героя:\n'
                       '1 - воин (ближний бой)\n'
                       '2 - лучник (дальний бой)\n'
                       '3 - маг (магия)\n'
                       'Каждый тип героя имеет повышенные шансы на случайную '
                       'максимальную атаку своего типа и случайный шанс '
                       'заблокировать атаку врага своего типа\n')
        if answer not in ('1', '2', '3'):
            print('Вы ввели что-то странное. '
                  'Пожалуйста, выведите и введите нормально.\n')
            sleep(1)
    selected_hero = choices[answer]().create_hero()
    return selected_hero


def finding_apple() -> None:
    """Увеличивает количество жизни героя на случайное число."""
    adding_health = randint(5, 50)
    print(f'Вы обнаружили волшебное яблоко,'
          f'которое увеличивает ваши жизни на {adding_health}!')
    hero.health += adding_health
    print(f'Теперь у вас {hero.health} жизней')


def finding_weapon() -> None:
    """Функция нахождения оружия."""
    variants = [SwordCreator, BowCreator, MagicianBookCreator]
    weapon = choice(variants)().create_weapon()
    print(f'Вы нашли новое оружие: {weapon.name} '
          f'(сила атаки: {weapon.min_attack}-{weapon.max_attack})')
    print('Ваше текущее оружие:')
    for item in hero.weapons.values():
        if item:
            print(f'{item.name}: {item.min_attack}-{item.max_attack}')

    answer = None
    while answer not in ("1", "2"):
        answer = input("Хотите его взять себе?\n1 - Да\n2 - Нет\n")
        if answer == '1':
            hero.weapons[weapon.name] = weapon
            print('Оружие теперь ваше! '
                  'Надеюсь, оно будет служить вам верой и правдой. Или нет.')
        elif answer == '2':
            print('Вы с горделивым видом шагаете мимо '
                  'этой бесполезной безделушки')
        else:
            print('Вы ввели что-то странное. '
                  'Пожалуйста, выведите и введите нормально.\n')


def finding_arrows() -> None:
    """Увеличивает количество стрел у героя на случайное число."""
    amount_arrows = randint(5, 15)
    print(f'Вы обнаружили {amount_arrows} стрел!')
    hero.arrows += amount_arrows
    print(f'Теперь у вас {hero.arrows} стрел')


def meeting_monster() -> None:
    """Функция встречи с врагом."""
    variants = [WarriorEnemyCreator, ArcherEnemyCreator, MagicianEnemyCreator]
    enemy = choice(variants)().create_enemy()
    print(f'Вам навстречу вышел враг: {enemy.name} '
          f'(сила атаки: {enemy.min_attack}-{enemy.max_attack}), '
          f'здоровье: {enemy.health}')

    answer = None
    while answer not in ("1", "2"):
        answer = input("Хотите вступить в битву или убежать?\n"
                       "1 - Я как не пацан что ли?\n"
                       "2 - Осторожность — мать мудрости\n")
        if answer == '1':
            print('Вы обнажаете клинки, или чего там у вас...')
            battle(hero, enemy)
        elif answer == '2':
            print('Надраться я ещё успею. Подраться, то есть.')
        else:
            print('Вы ввели что-то странное. '
                  'Пожалуйста, выведите и введите нормально.\n')


def finding_totem() -> None:
    """Функция, позволяющая сохранить игру или отказаться от этого."""
    print('Вы набрели на странное сооружение. '
          'На нём написано "Клонируй себя за пару секунд!"')

    answer = None
    while answer not in ("1", "2"):
        answer = input("Есть всего две кнопки:\n1 - Да\n2 - Нет\n")
        if answer == '1':
            save_game(hero)
            global saved_games_flag
            saved_games_flag = 1
            print('Аппарат странно загудел, за полупрозрачным стеклом '
                  'появилась фигура, смутно напоминающая вас.')
        elif answer == '2':
            print('Лучше это не трогать...')
        else:
            print('Вы ввели что-то странное. '
                  'Пожалуйста, выведите и введите нормально.\n')


def save_game(clone_of_hero: Hero) -> None:
    """Функция для сохранения объекта героя в файл."""
    with open('saved_game', 'wb') as game:
        pickle.dump(clone_of_hero, game)


def load_game() -> Hero:
    """Функция загрузки объекта героя из файла."""
    with open('saved_game', 'rb') as game:
        clone_of_hero = pickle.load(game)
        return clone_of_hero


def battle(my_hero: Hero, enemy: Enemy) -> None:
    """Функция, администрирующая ход битвы."""
    print('FIGHT!!!')
    while my_hero.health > 0 and enemy.health > 0:
        answer = None
        while answer not in ("1", "2"):
            answer = input("1 - Бей\n2 - Беги\n")
            if answer == '1':
                your_attack = my_hero.attack()
                print(f'Ты атакуешь противника с невиданной '
                      f'яростью: {your_attack}')
                enemy.health -= your_attack
                if enemy.health > 0:
                    enemy_attack = enemy.attack(my_hero)
                    print(f'В ответ прилетает '
                          f'не менее сильный удар {enemy_attack}')
                    my_hero.health -= enemy_attack
                    status()
            elif answer == '2':
                print('Убегаешь, делая вид, что забыл выключить дома утюг')
                return
            else:
                print('Вы ввели что-то странное. '
                      'Пожалуйста, выведите и введите нормально.\n')

    if my_hero.health <= 0 and saved_games_flag == 1:
        print('Кажется, сегодня не твой день, дружище :( ')
        answer = None
        while answer not in ("1", "2"):
            answer = input("1 - Загрузить сохранение\n2 - Rest In Peace\n")
            if answer == '1':
                global hero
                hero = load_game()
                print('Внезапно ты оказываешься в странном стеклянном '
                      'саркофаге. Тихое шипение, крышка открывается и '
                      'выпускат тебя наружу. Небольшое недоумение читается '
                      'в твоих глазах, однако подвиги не ждут! Вперед, герой!')
                return
            elif answer == '2':
                print('Конец игры...')
    elif my_hero.health <= 0 and saved_games_flag == 0:
        print('Кажется, сегодня не твой день, дружище :( ')
        print('Совсем не твой день...')
        print('Конец игры...')
    elif enemy.health <= 0:
        print('Ты поверг чудовищное порождение тьмы, мир стал чуть чище...')
        my_hero.defeated_monsters += 1
        if my_hero.defeated_monsters >= 10:
            print('Победа!!!')


actions = {1: finding_apple, 2: finding_weapon,
           3: finding_totem, 4: meeting_monster, 5: finding_arrows}

if __name__ == '__main__':
    hero = choice_of_hero()
    while hero.health > 0 and hero.defeated_monsters != 10:
        status()
        actions[randint(1, 5)]()
        print()
