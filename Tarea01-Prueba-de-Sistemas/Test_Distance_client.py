import unittest
from unittest.mock import patch
import distance_client


class TestCliente(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Latitud y Longitud Válidas
        cls.latitud_valida = 50
        cls.longitud_valida = 50

        # Latitud Inválida
        cls.latitud_menor_90_neg = -91
        cls.latitud_mayor_90 = 91

        # Longitud Inválida
        cls.longitud_menor_180_neg = -181
        cls.longitud_mayor_180 = 181

        # Unidad de Medida
        cls.unidad_km = "km"
        cls.unidad_nm = "nm"
        cls.unidad_invalida = "invalid"
        cls.unidad_vacia = ""

        # Valor inválido esperado
        cls.menos_uno = -1.0

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.latitud_menor_90_neg
        del cls.latitud_mayor_90
        del cls.longitud_menor_180_neg
        del cls.longitud_mayor_180
        del cls.latitud_valida
        del cls.longitud_valida
        del cls.unidad_km
        del cls.unidad_nm
        del cls.unidad_invalida
        del cls.menos_uno
    def test_latitud_menor_90_negativo(self):
        with patch("builtins.print") as mocked_print:
            distance_client.main(
                source=(self.latitud_menor_90_neg, self.longitud_valida),
                destination=(self.latitud_valida, self.longitud_valida),
                unit=self.unidad_km,
            )
            mocked_print.assert_any_call("Distance:", self.menos_uno)
            mocked_print.assert_any_call("Distance unit:", self.unidad_invalida)

    def test_latitud_mayor_90(self):
        with patch("builtins.print") as mocked_print:
            distance_client.main(
                source=(self.latitud_mayor_90, self.longitud_valida),
                destination=(self.latitud_valida, self.longitud_valida),
                unit=self.unidad_km,
            )
            mocked_print.assert_any_call("Distance:", self.menos_uno)
            mocked_print.assert_any_call("Distance unit:", self.unidad_invalida)

    def test_longitud_menor_180_negativo(self):
        with patch("builtins.print") as mocked_print:
            distance_client.main(
                source=(self.latitud_valida, self.longitud_menor_180_neg),
                destination=(self.latitud_valida, self.longitud_valida),
                unit=self.unidad_km,
            )
            mocked_print.assert_any_call("Distance:", self.menos_uno)
            mocked_print.assert_any_call("Distance unit:", self.unidad_invalida)

    def test_longitud_mayor_180(self):
        with patch("builtins.print") as mocked_print:
            distance_client.main(
                source=(self.latitud_valida, self.longitud_mayor_180),
                destination=(self.latitud_valida, self.longitud_valida),
                unit=self.unidad_km,
            )
            mocked_print.assert_any_call("Distance:", self.menos_uno)
            mocked_print.assert_any_call("Distance unit:", self.unidad_invalida)

    def test_unidad_invalida(self):
        with patch("builtins.print") as mocked_print:
            distance_client.main(
                source=(self.latitud_valida, self.longitud_valida),
                destination=(self.latitud_valida, self.longitud_valida),
                unit="miles",
            )
            mocked_print.assert_any_call("Distance:", self.menos_uno)
            mocked_print.assert_any_call("Distance unit:", self.unidad_invalida)

    def test_unidad_vacia(self):
        with patch("builtins.print") as mocked_print:
            distance_client.main(
                source=(self.latitud_valida, self.longitud_valida),
                destination=(self.latitud_valida, self.longitud_valida),
                unit=self.unidad_vacia,
            )
            mocked_print.assert_any_call("Distance unit:", "km")


if __name__ == "__main__":
    unittest.main()
