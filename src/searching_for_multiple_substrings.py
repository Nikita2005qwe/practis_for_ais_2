"""
Основной модуль программы
поиск нескольких подстрок
"""
from search import search
from max_len_str import calculate_max_len_str_in_str_tuple
import argparse
from colorama import Fore, Style, init
from random import randint


def go_answer(string: str, sub_strings: tuple[str]):
    """
    функция для выводи цветного ответа
    :param string: str
    :param sub_strings: tuple[str]
    :return: str
    """
    # объявляем массив цветов
    list_of_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    # Инициализация colorama
    init(autoreset=True)
    # Заменяем подстроку на цветной аналог
    for sub in sub_strings:
        color = list_of_colors.pop(randint(0, len(list_of_colors)-1))
        string = string.replace(sub, f"{color}{sub}{Style.RESET_ALL}")
        if not list_of_colors:
            list_of_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    
    return string


def main():
    """
    Точка входа в программу
    :return: None
    """
    parser = argparse.ArgumentParser(description="Алгоритм поиска подстрок")
    parser.add_argument("string", help="Строка")
    parser.add_argument("sub_strings", type=str, help="Подстроки")
    parser.add_argument('-cs', '--case_sensitivity', type=bool, default=False)
    parser.add_argument('-m', '--method', type=str, default='first')
    parser.add_argument('-c', '--count', type=int, default=10)
    args = parser.parse_args()
    
    string = args.string
    sub_strings = args.sub_strings
    sub_strings = tuple(sub_strings.split(','))
    case_sensitivity = args.case_sensitivity
    method = args.method
    count = args.count
    
    result = search(string, sub_strings, case_sensitivity, method, count)
    print(f"{result}")
    print(go_answer(string, sub_strings))


if __name__ == "__main__":
    main()
