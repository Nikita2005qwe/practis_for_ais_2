def calculate_max_len_str_in_str_tuple(tuple_str: tuple[str]):
    """
    Функиця для подсчёта максимальной по длинне строки в кортеже
    :param tuple_str: tuple[str]
    :return: str
    """
    max_len_str = ""
    for i in tuple_str:
        if len(max_len_str) < len(i):
            max_len_str = i
    return max_len_str
    