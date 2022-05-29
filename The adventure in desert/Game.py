from Interlude import beginning_of_the_game as bg
from Challenge_1 import challenge_1 as ch1
from Challenge_2 import challenge_2 as ch2


question = input("Хотите ли вы начать игру?: ")
bg(question)

knight_hp_points = ch1(2)  # Вводим количество жизней у рыцаря. Оптимально - от 1 до 3 шт.

if knight_hp_points != 0:  # Смог продолжить игру c 0 хп, табуляция была неверной

# Начало заключительного испытания
    win_combination = ["Воин", "Меч", "Магия"]
    ch2(win_combination)


