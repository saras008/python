#import module aritmatik.py
import aritmatik
import unittest

class Test_addition(unittest.TestCase):
    def test_add_number_int(self):
        sums = aritmatik.add_number(50,50)
        self.assertEqual(sums,100)
    def test_add_number_float(self):
        sums = aritmatik.add_number(50.2,50.3)
        self.assertEqual(sums,100.5)

    def test_add_number_string(self):
        sums = aritmatik.add_number('hello','world')
        self.assertEqual(sums,'helloworld')


if __name__ == '__main__':
    unittest.main()

