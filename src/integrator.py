import numpy as np
from src.preprocess_img import preprocess
from src.load_model import model_fun
from src.grad_cam import grad_cam

def predict(array):
    """
    Coordinador de módulos: Unifica las salidas para la interfaz gráfica.
    Realiza el preprocesamiento, la predicción y genera el heatmap.
    """
    # 1. Preprocesamiento
    batch_array_img = preprocess(array)
    
    # 2. Carga del modelo y predicción
    model = model_fun()
    prediction = np.argmax(model.predict(batch_array_img))
    proba = np.max(model.predict(batch_array_img)) * 100
    
    label = ""
    if prediction == 0:
        label = "bacteriana"
    elif prediction == 1:
        label = "normal"
    elif prediction == 2:
        label = "viral"
        
    # 3. Generación del mapa de calor
    heatmap = grad_cam(array)
    
    return label, proba, heatmap
