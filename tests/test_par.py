# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import numero_par

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_numero_par(self):
        assert numero_par(4)
        assert numero_par(7)
        assert numero_par(33)
        assert numero_par(52)
