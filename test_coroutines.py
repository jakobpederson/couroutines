import unittest
import coroutines


class CoroutinesTest(unittest.TestCase):

    def test_print_number(self):
        test_co = coroutines.print_number()
        for i in range(1, 6):
            test_co.send(i)
        try:
            test_co.send(None)
        except StopIteration as exc:
            result = exc.value
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_print_and_return_number(self):
        test_co = coroutines.print_and_return_number()
        for i in range(1, 6):
            print(test_co.send(i))
            next(test_co)
        result = coroutines.terminate_coroutine(test_co)
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_complex_print(self):
        from contextlib import redirect_stdout
        from io import StringIO
        out = StringIO()
        with redirect_stdout(out):
            test_co = coroutines.complex_print(2)
            test_co_5 = coroutines.complex_print(5)
            test_co_5.send(2)
            test_co.send(9)
            test_co_5.send(3)
        result = out.getvalue().strip().split('\n')
        self.assertEqual(['10', '18', '15'], result)

    def test_super_complicated_example(self):
        test_co = coroutines.super_complicated_example()
        test_co.send('Jakob Pederson')
        test_co.send('Caleb Salt')
        first, last = coroutines.terminate_coroutine(test_co)
        self.assertEqual(['Jakob', 'Caleb'], first)
        self.assertEqual(['Pederson', 'Salt'], last)
