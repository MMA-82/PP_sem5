"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии
"""

from random import randint


def calc_bonus(names: list[str], rates: list[int], percs: list[str]) -> dict:
    """
    Возвращает словарь с премиями по именам.
    """
    calc = {name: round((rate * float(perc[:-1]) / 100, 2) for name, rate, perc in zip(names, rates, percs)}
    # calc = {}
    # for name, rate, perc in zip(names, rates, percs):
    #     perc = float(perc[:-1])
    #     calc[name] = round((rate * perc/100), 2)
    return calc


if __name__ == '__main__':
    names = ['Олег', 'Иван', 'Сергей']
    rates = [randint(50, 70) for i in range(3)]
    percs = ['10.25%', '12.05%', '9.50%']
    print(f'Премии:{calc_bonus(names, rates, percs)}')
