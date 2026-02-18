import unittest
from math_utils import es_par

class TestEsPar(unittest.TestCase):

    def test_numero_par(self):
        self.assertTrue(es_par(4))

    def test_numero_impar(self):
        self.assertFalse(es_par(5))

    def test_cero_es_par(self):
        self.assertTrue(es_par(0))

    def test_negativo_par(self):
        self.assertTrue(es_par(-2))

    def test_negativo_impar(self):
        self.assertFalse(es_par(-3))

if __name__ == "__main__":
    unittest.main()