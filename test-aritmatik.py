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

class Test_Subtitution(unittest.TestCase):
    def test_subs_number_int(self):
        subs = aritmatik.sub_number(50,25)
        self.assertEqual(subs,25)

    def test_subs_number_float(self):
        subs=aritmatik.sub_number(75.2,25.2)
        self.assertEqual(subs,50.0)
    
class Test_divs(unittest.TestCase):
    def test_divs_number_int(self):
        divs= aritmatik.divs_number(4,2)
        self.assertEqual(divs,2)

    def test_divs_number_float(self):
        divs=aritmatik.divs_number(20.2,2)
        self.assertEqual(divs,10.1)

class Test_multiple(unittest.TestCase):
    def test_multi_number_int(self):
        multi = aritmatik.multi_number(3,3)
        self.assertEqual(multi,9)
    def test_multi_number_float(self):
        multi=aritmatik.multi_number(7.0,7)
        self.assertEqual(multi,49.0)
if __name__ == '__main__':
    unittest.main()

