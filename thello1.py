# tkal1.py
import unittest
import helou

class test_kalkulator(unittest.TestCase):
    def test_helou(self):
        wynik = helou.SayHello()
        self.assertEqual(wynik,'Hello World')
        self.assertNotEqual(wynik,'bla bla bla')



if __name__=='__main__':
    unittest.main()
