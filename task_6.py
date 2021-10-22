import itertools
import unittest
from typing import Callable, Union


class AstTester(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @staticmethod
    def get_new_arglist(arglist: dict):
        new_data = {}
        for key, val in arglist.items():
            if isinstance(key, int):
                new_data[key] = val
            else:
                new_data[key] = [{key: v} for v in val]
        return new_data

    @staticmethod
    def get_args_kwargs_from_row(row: Union[list, tuple]):
        args, kwargs = [], {}
        for el in row:
            if isinstance(el, dict):
                kwargs.update(el)
            else:
                args.append(el)
        return args, kwargs

    def fun_matrix(self, u_fun: Callable, a_fun: Callable, arglist: dict, m: str = ''):
        new_arglist = self.get_new_arglist(arglist=arglist)
        for input_data in itertools.product(*new_arglist.values()):
            args, kwargs = self.get_args_kwargs_from_row(row=input_data)
            result_user_func = u_fun(*args, **kwargs)
            result_reference_func = a_fun(*args, **kwargs)
            error_msg = (
                "Результат пользовательской функции отличается от результата функции авторского решения!\n"
                f"Аргументы = {args} | Позиционные аргументы: = {kwargs}"
            )
            self.assertEqual(result_user_func, result_reference_func, error_msg)
