import if_example
import unittest

class Test_If(unittest.TestCase):
    def test_if(self):
        hasil = if_example.check_if()
        self.assertEqual(hasil,100)

if __name__ == '__main__':
    unittest.main()
