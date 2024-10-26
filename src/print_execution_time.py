from time import time

def print_execution_time(function: callable):
    """
    Декоратор для логирования времени выполнения скрипта
    :param function: callable
    :return:
    """
    def timed(*args, **kw):
        """
        функция замеряющая время выполнения функции function
        аргументы для функции
        :param args:
        :param kw:
        :return:
        """
        time_start = time()
        return_value = function(*args, **kw)
        time_end = time()

        execution_time = time_end - time_start

        arguments = ", ".join(
            [str(arg) for arg in args] + ["{}={}".format(k, kw[k]) for k in kw]
        )

        print(
            "{} ms {}({})".format(
                str(execution_time*1000), function.__name__, arguments
            )
        )
        return return_value

    return timed
