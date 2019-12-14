# test_ptogram1.py
import unittest
import moj_program

class Test1TDD(unittest.TestCase):
    def test_100(self):
        wynik = moj_program.zwroc_100()
        self.assertEqual(100,wynik)
    def test_par(self):
        wyn = moj_program.zwroc_par('ala')
        self.assertEqual('ala',wyn)

if __name__=='__main__':
    unittest.main()
