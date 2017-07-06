from contextlib import redirect_stdout
import coroutines
from io import StringIO
import unittest


class CoroutinesTest(unittest.TestCase):

    def test_print_number(self):
        print_number = coroutines.print_number()
        for i in range(1, 6):
            print_number.send(i)
        result = coroutines.terminate_coroutine(print_number)
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_print_and_yield_number(self):
        print_and_yield = coroutines.print_and_yield_number()
        for i in range(1, 6):
            print(print_and_yield.send(i))
            next(print_and_yield)
        result = coroutines.terminate_coroutine(print_and_yield)
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_multiply_number_by_var(self):
        out = StringIO()
        with redirect_stdout(out):
            multiply_by_2 = coroutines.multiply_number_by_var(2)
            multiply_by_5 = coroutines.multiply_number_by_var(5)
            multiply_by_5.send(2)
            multiply_by_2.send(9)
            multiply_by_5.send(3)
        result = out.getvalue().strip().split('\n')
        self.assertEqual(['10', '18', '15'], result)

    def test_coroutine_to_coroutines(self):
        names = coroutines.coroutine_to_coroutines(coroutines.get_list_of_names, coroutines.print_number)
        names.send('Jakob Pederson')
        names.send('Caleb Salt')
        first, last = coroutines.terminate_coroutine(names)
        self.assertEqual(['Jakob', 'Caleb'], first)
        self.assertEqual(['Pederson', 'Salt'], last)
