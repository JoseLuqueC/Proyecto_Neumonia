import tensorflow as tf
import os
import warnings

# Ocultar warnings de TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')

# Deshabilitar ejecución eager (requerido por el código original de keras/tf)
tf.compat.v1.disable_eager_execution()
tf.compat.v1.experimental.output_all_intermediates(True)

def model_fun(model_path='conv_MLP_84.h5'):
    """
    Carga y retorna el modelo H5 preentrenado.
    """
    model = tf.keras.models.load_model(model_path)
    return model
