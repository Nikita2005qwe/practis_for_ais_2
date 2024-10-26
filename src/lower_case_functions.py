"""
Модуль для функций lower_case и lower_case_to_multiple_substrings
"""

def lower_case(case_sensitivity: bool, string: str, sub_string: str):
    """
    Метод для того, чтобы строку string подстроку sub_string сделать маленькими
    """
    if not case_sensitivity:
        string = string.lower()
        sub_string = sub_string.lower()
    return string, sub_string


def lower_case_to_multiple_substrings(case_sensitivity: bool, string: str, sub_string: tuple[str]):
    """
    Метод для того, чтобы строку string все подстроки sub_string сделать маленькими
    """
    if sub_string == ():
        return string, sub_string
   
    if not case_sensitivity:
        sub_strings = []
        string = string.lower()
        for sub in sub_string:
            sub_strings.append(sub.lower())
        return string, tuple(sub_strings)
    return string, sub_string
