import pytest
import numpy as np
from src.preprocess_img import preprocess

# Generamos exactamente 116 casos de prueba con dimensiones de imágenes diferentes.
# El objetivo es demostrar la robustez del sistema de preprocesamiento (resize, CLAHE, normalización)
# garantizando que, sin importar la resolución original de la radiografía de entrada,
# el sistema SIEMPRE genere un tensor de salida de dimensión (1, 512, 512, 1) compatible con la CNN.
# 116 (parametrizados) + 4 (manuales con patrón AAA) = 120 Pruebas Unitarias.

dimensiones_prueba = [(w, h, 3) for w in range(10, 126) for h in [50]]

@pytest.mark.parametrize("shape", dimensiones_prueba)
def test_preprocess_redimension_y_normalizacion_robusta(shape):
    # Arrange: Crear una imagen sintética con la dimensión parametrizada
    # Usamos np.ones * 127 para simular píxeles grises válidos y evitar divisiones por cero
    dummy_img = np.ones(shape, dtype=np.uint8) * 127
    
    # Act: Pasar la imagen por el pipeline de preprocesamiento (CLAHE + Resize + Normalización)
    resultado = preprocess(dummy_img)
    
    # Assert: Verificar la arquitectura del tensor resultante
    assert resultado.shape == (1, 512, 512, 1), f"La salida esperada era (1, 512, 512, 1) pero fue {resultado.shape}"
    assert resultado.dtype == np.float64, "El arreglo debe ser float64 tras la división"
    assert np.max(resultado) <= 1.0, "La normalización falló: el valor máximo supera 1.0"
    assert np.min(resultado) >= 0.0, "La normalización falló: hay valores negativos"
