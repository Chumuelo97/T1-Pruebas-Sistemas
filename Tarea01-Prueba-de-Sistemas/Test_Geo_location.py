import unittest
from geo_location import Position

class TestPosition(unittest.TestCase):

    # Caso de prueba para latitud menor a -90 (inválida)
    def test_menor_90_negativo_latitud(self):
        with self.assertRaises(ValueError):
            Position(latitude=-91, longitude=20, altitude=0)

    # Caso de prueba para latitud mayor a 90 (inválida)
    def test_mayor_90_latitud(self):
        with self.assertRaises(ValueError):
            Position(latitude=91, longitude=20, altitude=0)

    # Caso de prueba para latitud en el límite inferior (-90, válida)
    def test_limite_inferior_valido_latitud(self):
        try:
            Position(latitude=-90, longitude=20, altitude=0)
        except ValueError:
            self.fail("Position raised ValueError unexpectedly for latitud = -90")

    # Caso de prueba para latitud en el límite superior (90, válida)
    def test_limite_superior_valido_latitud(self):
        try:
            Position(latitude=90, longitude=20, altitude=0)
        except ValueError:
            self.fail("Position raised ValueError unexpectedly for latitud = 90")

    # Caso de prueba para longitud menor a -180 (inválida)
    def test_menor_180_negativo_longitud(self):
        with self.assertRaises(ValueError):
            Position(latitude=20, longitude=-181, altitude=0)

    # Caso de prueba para longitud mayor a 180 (inválida)
    def test_mayor_180_longitud(self):
        with self.assertRaises(ValueError):
            Position(latitude=20, longitude=181, altitude=0)

    # Caso de prueba para longitud en el límite inferior (-180, válida)
    def test_limite_inferior_valido_longitud(self):
        try:
            Position(latitude=20, longitude=-180, altitude=0)
        except ValueError:
            self.fail("Position raised ValueError unexpectedly for longitud = -180")

    # Caso de prueba para longitud en el límite superior (180, válida)
    def test_limite_superior_valido_longitud(self):
        try:
            Position(latitude=20, longitude=180, altitude=0)
        except ValueError:
            self.fail("Position raised ValueError unexpectedly for longitud = 180")

if __name__ == '__main__':
    unittest.main()
