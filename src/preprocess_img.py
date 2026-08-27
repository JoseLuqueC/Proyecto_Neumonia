import cv2
import numpy as np

def preprocess(array: np.ndarray) -> np.ndarray:
    """
    Realiza el preprocesamiento de la imagen según la rúbrica:
    Resize 512x512, Escala de grises, CLAHE, Normalización (0-1)
    """
    array = cv2.resize(array, (512, 512))
    
    # Si la imagen tiene 3 canales (RGB), la pasamos a escala de grises
    if len(array.shape) == 3:
        array = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
        
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))
    array = clahe.apply(array)
    
    # Normalización (0-1)
    array = array / 255.0
    
    array = np.expand_dims(array, axis=-1)
    array = np.expand_dims(array, axis=0)
    return array
