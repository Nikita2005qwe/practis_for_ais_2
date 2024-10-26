"""
Модуль с алгоритмом KMP и префикс функцией prefix_function
"""
from max_len_str import calculate_max_len_str_in_str_tuple


def KMP_applicable_to_multiple_substrings(string: str, sub_strings: tuple[str], count: int, method: str = 'first') -> dict:
    # необходимо составить матрицу и список подстрок
    # затем по столбцам матрицы добавлять в словарь индексы на нужные позиции
    if count <= 0:
        return None
    old_dict_of_index = {i: None for i in sub_strings}
    new_dict_of_index = {i: None for i in sub_strings}  # словарь со значениями индексов вхождений для каждой подстроки
    max_len_of_sub_strings = calculate_max_len_str_in_str_tuple(sub_strings)
    # матрица для значений функции префиксов
    matrix_result_of_prefix_function: list[list[int]] = []
    for i in sub_strings:
        string_for_prefix_function: str = i + "#" + string
        list_result_of_prefix_function: list[int] = prefix_function(string_for_prefix_function)
        matrix_result_of_prefix_function.append(list_result_of_prefix_function)
    # ищем на каких позициях значения массива совпадают со значением m
    if method == 'first':
        # поиск в прямом порядке
        flag_finish = False
        for j in range(1, len(max_len_of_sub_strings)+len(string)+1):
            for i, sub_string in zip(matrix_result_of_prefix_function, sub_strings):
                try:
                    if len(sub_string) == i[j]:
                        if new_dict_of_index[sub_string] is None:
                            new_dict_of_index[sub_string] = (j - 2*len(sub_string),)
                        else:
                            tuple_0 = new_dict_of_index[sub_string]
                            new_dict_of_index[sub_string] = tuple_0.__add__((j - 2*len(sub_string),))
                        count -= 1
                except IndexError:
                    pass
                if count == 0:
                    flag_finish = True
                    break
            
            if flag_finish is True:
                break

    elif method == 'last':
        # поиск в обратном порядке
        flag_finish = False
        list_of_index_j = list(range(1, len(max_len_of_sub_strings) + len(string)+1))
        list_of_index_j.reverse()
        for j in list_of_index_j:
            for i, sub_string in zip(matrix_result_of_prefix_function, sub_strings):
                try:
                    if len(sub_string) == i[j]:
                        if new_dict_of_index[sub_string] is None:
                            new_dict_of_index[sub_string] = (j - 2 * len(sub_string),)
                        else:
                            tuple_0 = new_dict_of_index[sub_string]
                            new_dict_of_index[sub_string] = tuple_0.__add__((j - 2 * len(sub_string),))
                        count -= 1
                except IndexError:
                    continue
                if count == 0:
                    flag_finish = True
                    break
            if flag_finish is True:
                break

    if old_dict_of_index == new_dict_of_index:
        return None

    return new_dict_of_index


def KMP(string: str, sub_string: str, count: int, method: str = 'first') -> list[int]:
    """
    Реализация аглоритма КМП
    """
    list_of_index = []
    m = len(sub_string)
    n = len(string)
    string_for_prefix_function: str = sub_string+"#"+string
    list_result_of_prefix_function: list[int] = prefix_function(string_for_prefix_function)
    # ищем на каких позициях значения массива совпадают со значением m
    if method == 'first':
        # поиск в прямом порядке
        for i in range(m+1, n+m+1):
            if list_result_of_prefix_function[i] == m:
                list_of_index.append(i-2*m)
                if count <= len(list_of_index):
                    break
    
    elif method == 'last':
        # поиск в обратном порядке
        list_of_index_i = list(range(m+1, n+m+1))
        list_of_index_i.reverse()
        for i in list_of_index_i:
            if list_result_of_prefix_function[i] == m:
                list_of_index.append(i-2*m)
                if count <= len(list_of_index):
                    break
    
    if len(list_of_index) == 0:
        return None
    
    return list_of_index
    

def prefix_function(string: str) -> list[int]:
    """
    Префикс функция для первого шага в алгоритме КМП
    p - массив натуральных чисел, определяется как максимальная длина собственного префикса, совпадающего с суффиксом
    """
    len_of_string = len(string)
    p = [0]*len_of_string  # первый элемент будет равен 0 так как строка не имеет суффикса (длина 1)
    j = 0
    i = 1
    while i < len_of_string:
        if string[i] == string[j]:
            p[i] = j + 1
            j += 1
            i += 1
        elif j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]
    return p

# не обязательный метод
def print_dict(current_dict):
    if len(current_dict) == 1:
        for i in current_dict:
            print(current_dict[i])
    elif len(current_dict) > 1:
        for i in current_dict:
            print(i + ": " + str(current_dict[i]))
    else:
        print("error, dict is empty")


