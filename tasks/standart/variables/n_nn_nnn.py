"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Отредактировать функцию n_sum, которая принимает целое число n, таким образом,
чтобы она возвращала n+nn+nnn

ПРИМЕРЫ
--------------------------------------------------------------------------------
n_sum(1) -> 3, т.к. 1+1+1=3
n_sum(3) -> 39, т.к. 3+9+27=39
"""


def n_sum(n: int) -> int:
    """
    Вычисляет формулу n+nn+nnn

    :param n: некоторое целое число

    :return: результат выполнения
    """

    return n + n**2 + n**3


if __name__ == '__main__':
    n_number = int(input('Введите число n: '))
    print(f'Результат n+nn+nnn: {n_sum(n_number)}')
