import pytest
import numpy as np
from src.preprocess_img import preprocess

class TestPreprocessImg:
    
    def test_preprocess_returns_correct_dimensions_for_rgb(self):
        """
        Prueba que el preprocesamiento de una imagen RGB devuelva el shape esperado (1, 512, 512, 1)
        """
        # Arrange (Preparar)
        # Simulamos una imagen RGB de 100x100 píxeles
        dummy_rgb_image = np.zeros((100, 100, 3), dtype=np.uint8)
        
        # Act (Actuar)
        result = preprocess(dummy_rgb_image)
        
        # Assert (Afirmar)
        assert result.shape == (1, 512, 512, 1), f"Shape incorrecto: {result.shape}"

    def test_preprocess_returns_correct_dimensions_for_grayscale(self):
        """
        Prueba que el preprocesamiento de una imagen en escala de grises devuelva el shape esperado.
        """
        # Arrange (Preparar)
        # Simulamos una imagen Grises de 256x256 píxeles
        dummy_gray_image = np.zeros((256, 256), dtype=np.uint8)
        
        # Act (Actuar)
        result = preprocess(dummy_gray_image)
        
        # Assert (Afirmar)
        assert result.shape == (1, 512, 512, 1), f"Shape incorrecto: {result.shape}"
        
    def test_preprocess_normalizes_values(self):
        """
        Prueba que el preprocesamiento normalice los píxeles entre 0 y 1.
        """
        # Arrange (Preparar)
        dummy_image = np.ones((50, 50, 3), dtype=np.uint8) * 200 # Valores de píxeles en 200
        
        # Act (Actuar)
        result = preprocess(dummy_image)
        
        # Assert (Afirmar)
        assert np.max(result) <= 1.0, "El valor máximo supera 1.0"
        assert np.min(result) >= 0.0, "El valor mínimo es menor a 0.0"
