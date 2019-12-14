# test_ptogram1.py
import unittest
import moj_program

class Test1TDD(unittest.TestCase):
    def test_100(self):
        wynik = moj_program.zwroc_100()
        self.assertEqual(100,wynik)

    def zwroc_parametr(self):
        ret = moj_program.zwroc_parametr('ala')
        self.assertEqual(ret,'ala')

if __name__=='__main__':
    unittest.main()
