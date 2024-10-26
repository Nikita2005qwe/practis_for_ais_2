"""
Основной модуль программы
поиск одной подстроки
"""
from search import search
from max_len_str import calculate_max_len_str_in_str_tuple
import argparse
from colorama import Fore, Style, init

def go_answer(string: str, sub_string):
    """
    функция для выводи цветного ответа
    :param string: str
    :param sub_string: tuple[str]
    :return: str
    """
    # Инициализация colorama
    init(autoreset=True)
    # Заменяем подстроку на цветной аналог
    highlighted_text = string.replace(sub_string, f"{Fore.RED}{sub_string}{Style.RESET_ALL}")
    
    return highlighted_text
    

def main():
    """
    Точка входа в программу
    :return: None
    """
    parser = argparse.ArgumentParser(description="Алгоритм поиска подстрок")
    parser.add_argument("string", help="Строка")
    parser.add_argument("sub_string", help="Подстрока")
    parser.add_argument('-cs', '--case_sensitivity', type=bool, default=False)
    parser.add_argument('-m', '--method', type=str, default='first')
    parser.add_argument('-c', '--count', type=int, default=10)
    args = parser.parse_args()
    
    string = args.string
    sub_string = args.sub_string
    case_sensitivity = args.case_sensitivity
    method = args.method
    count = args.count
    
    result = search(string, sub_string, case_sensitivity, method, count)
    print(f"{result}")
    print(go_answer(string, sub_string))
    

if __name__ == "__main__":
    main()
    