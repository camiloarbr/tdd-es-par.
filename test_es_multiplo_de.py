import unittest
from math_utils import es_multiplo_de

class TestEsMultiploDe(unittest.TestCase):

    def test_multiplo_positivo(self):
        self.assertTrue(es_multiplo_de(10, 2))

    def test_no_multiplo_positivo(self):
        self.assertFalse(es_multiplo_de(10, 3))

    def test_cero_es_multiplo_de_cualquier_numero(self):
        self.assertTrue(es_multiplo_de(0, 5))

    def test_m_es_cero(self):
        self.assertFalse(es_multiplo_de(10, 0))

    def test_n_negativo_multiplo(self):
        self.assertTrue(es_multiplo_de(-6, 3))

    def test_n_negativo_no_multiplo(self):
        self.assertFalse(es_multiplo_de(-7, 3))

    def test_ambos_negativos(self):
        self.assertTrue(es_multiplo_de(-6, -3))

    def test_m_negativo(self):
        self.assertTrue(es_multiplo_de(6, -3))

if __name__ == "__main__":
    unittest.main()