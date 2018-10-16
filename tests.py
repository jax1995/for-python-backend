import unittest
from gcd import gcd


class TestNod(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(gcd(0, 0), 0)
        
    def test_ones(self):
        j = 0
        for m, n, nod in (0, 1, 1), (1, 0, 1), (1, 1, 1), (2, 1, 1), (1, 2, 1), (3, 1, 1), (1, 3, 1):
            with self.subTest(i=j):
                self.assertEqual(gcd(m, n), nod) 
            j += 1
    def test_odd(self):
        j = 0
        for m, n, nod in (3, 3, 3), (5, 3, 1), (3, 5, 1), (5, 5, 5):
            with self.subTest(i=j):
                self.assertEqual(gcd(m, n), nod) 
            j += 1 
    def test_even(self):
        j = 0
        for m, n, nod in (2, 2, 2), (4, 2, 2), (2, 4, 2), (4, 4, 4):
            with self.subTest(i=j):
                self.assertEqual(gcd(m, n), nod) 
            j += 1

    def test_even_odd(self):
        j = 0
        for m, n, nod in (2, 3, 1), (3, 2, 1), (4, 5, 1), (5, 4, 1):
            with self.subTest(i=j):
                self.assertEqual(gcd(m, n), nod) 
            j += 1
   
if __name__ == '__main__':
    unittest.main()
