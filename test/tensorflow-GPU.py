import tensorflow as tf

print("TensorFlow version:", tf.__version__)
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("GPU is available:", gpus)
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)  # Avoid memory errors
else:
    print("GPU not available, running on CPU")
