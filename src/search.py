"""Шаблон модуля search"""
from typing import Optional
from print_execution_time import print_execution_time
from docx import Document
from KMP import KMP_applicable_to_multiple_substrings, KMP
from lower_case_functions import lower_case, lower_case_to_multiple_substrings

@print_execution_time
def search(string: str, sub_string, case_sensitivity: bool = False, method='first', count: Optional[int] = None):
    """
    Алгоритм поиска подстрок sub_string в колличестве count
    """
    if count is None:
        count = len(string)
    
    result = None
    if type(sub_string) == type((1,)):
        string, sub_string = lower_case_to_multiple_substrings(case_sensitivity, string, sub_string)
        result = KMP_applicable_to_multiple_substrings(string, sub_string, count, method)
    elif type(sub_string) == type("a"):
        string, sub_string = lower_case(case_sensitivity, string, sub_string)
        result = KMP(string, sub_string, count, method)
        if result is not None:
            result = tuple(result)
    
    return result

@print_execution_time
def search_in_file(file_name: str, sub_string, case_sensitivity: bool = False, method: str = 'first', count: Optional[int] = None):
    """
    Метод для поиска подстрок в файле
    :param file_name: str
    :param sub_string: str | tuple[str]
    :param case_sensitivity: bool
    :param method: str = 'first'
    :param count: Optional[int]
    :return:
    """
    data: str = ""
    # поиск в текстовом файле
    if file_name.endswith(".txt"):
        with open(file_name, encoding="utf-8") as file:
            for string in file:
                data += string.rstrip()
            
    # поиск в архивированном файле
    elif file_name.endswith(".docx"):
        doc: Document = Document(file_name)
        for paragraph in doc.paragraphs:
            data += paragraph.text
    
    # не определённый формат файла
    else:
        return None
    return search(data, sub_string, case_sensitivity, method, count)


if __name__ == "__main__":
    res1 = search_in_file(
        file_name="test/first.txt",
        sub_string="aba")
    res2 = search_in_file(
        file_name="test/first.txt",
        sub_string=("aaa", "bba"))
    
    res3 = search_in_file(
        file_name="test/second.docx",
        sub_string=("aaa", "bba"))
    res4 = search_in_file(
        file_name="test/second.docx",
        sub_string="aba")
    
    print(res1 == res4)
    print(res2 == res3)
    