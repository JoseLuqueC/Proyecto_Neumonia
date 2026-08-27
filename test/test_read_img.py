import pytest
import numpy as np
from src.read_img import read_jpg_file
import cv2
import os

class TestReadImg:
    
    # Creamos un archivo JPG temporal antes de probar (Setup)
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        # Arrange global (Crear imagen de prueba)
        self.test_image_path = "test_dummy.jpg"
        dummy_img = np.ones((50, 50, 3), dtype=np.uint8) * 255
        cv2.imwrite(self.test_image_path, dummy_img)
        
        yield # Aquí se ejecutan los tests
        
        # Limpiar al terminar
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)

    def test_read_jpg_file_returns_correct_types(self):
        """
        Verifica que read_jpg_file retorne un arreglo NumPy y un objeto Image de PIL.
        """
        # Arrange (Preparar) - La imagen ya fue creada en el fixture
        from PIL.Image import Image
        
        # Act (Actuar)
        img_array, img_pil = read_jpg_file(self.test_image_path)
        
        # Assert (Afirmar)
        assert isinstance(img_array, np.ndarray), "El primer valor no es un arreglo numpy"
        assert isinstance(img_pil, Image), "El segundo valor no es un objeto Pillow Image"
