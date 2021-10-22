import time
from enum import Enum
from typing import Callable


class TimeMeasure(Enum):
    s = 1
    ms = 1000


def timer(measure: TimeMeasure):
    if not isinstance(measure, TimeMeasure):
        raise ValueError('Декоратор принимает на вход только enum-объект TimeMeasure')

    def wrapped(func: Callable):
        def wrapper(*args, **kwargs):
            print(f"Выполняем фукнцию {func.__name__}")
            start_time = time.time()
            res = func(*args, **kwargs)
            end = round((time.time() - start_time) * measure.value, 2)
            time_type = "секунд(ы/у)" if measure.value == 1 else "миллисекунд(ы/у)"
            print(f"Функция {func.__name__} выполнилась за {end} {time_type}")
            return res

        return wrapper

    return wrapped


@timer(TimeMeasure.s)
def some_func_1():
    time.sleep(5)


@timer(TimeMeasure.ms)
def some_func_2():
    time.sleep(5)


some_func_1()
some_func_2()
