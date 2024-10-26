def connecting_tuples(list_of_tuples: list[tuple]):
    """
    Возвращает кортеж склеенный из кортежей
    находящихся в list_of_tuples
    
    :param list_of_tuples: list[tuple]
    :return: Optional[tuple]
    """
    mega_tuple = ()
    for _tuple in list_of_tuples:
        if _tuple is not None:
            mega_tuple += _tuple
    
    if mega_tuple == ():
        return None
    
    return mega_tuple
