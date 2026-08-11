import tensorflow as tf
import os
import warnings

# Eliminar explícitamente el mensaje de oneDNN
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# Ocultar warnings menores de C++
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')

# Ya NO necesitamos disable_eager_execution() porque modernizamos Grad-CAM a TensorFlow 2.x

def model_fun(model_path='conv_MLP_84.h5'):
    """
    Carga y retorna el modelo H5 preentrenado.
    """
    model = tf.keras.models.load_model(model_path)
    return model
