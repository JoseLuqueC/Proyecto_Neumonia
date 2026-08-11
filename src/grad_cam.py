import numpy as np
import cv2
import tensorflow as tf
from src.preprocess_img import preprocess
from src.load_model import model_fun

def grad_cam(array):
    """
    Genera el mapa de calor (Grad-CAM) para explicar la predicción.
    Migrado a TensorFlow 2.x (GradientTape) para eliminar los warnings de ejecución Eager.
    """
    img = preprocess(array)
    model = model_fun()
    
    # 1. Creamos un modelo auxiliar que escupe los Feature Maps y las Predicciones
    last_conv_layer = model.get_layer("conv10_thisone")
    grad_model = tf.keras.models.Model(
        inputs=[model.inputs],
        outputs=[last_conv_layer.output, model.output]
    )
    
    # 2. Usamos GradientTape (La forma moderna de TF 2.x) en lugar de K.gradients
    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img)
        pred_index = tf.argmax(predictions[0])
        loss = predictions[:, pred_index]
        
    # 3. Calculamos los gradientes
    grads = tape.gradient(loss, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    
    # 4. Multiplicamos la salida convolucional por los gradientes
    conv_outputs = conv_outputs[0]
    heatmap = conv_outputs @ tf.expand_dims(pooled_grads, -1)
    heatmap = tf.squeeze(heatmap)
    
    # 5. Normalizamos (ReLU)
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    heatmap = heatmap.numpy()
    
    # 6. Colorear y superponer (OpenCV)
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[2]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    
    img2 = cv2.resize(array, (512, 512))
    hif = 0.8
    transparency = heatmap * hif
    transparency = transparency.astype(np.uint8)
    
    superimposed_img = cv2.add(transparency, img2)
    superimposed_img = superimposed_img.astype(np.uint8)
    
    return superimposed_img[:, :, ::-1]
