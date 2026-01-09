import tensorflow as tf

# 1. Check for physical GPU device
gpu_devices = tf.config.list_physical_devices('GPU')
print(f"GPU devices detected: {gpu_devices}")

# 2. Check if Metal is specifically listed
if any("GPU" in str(device) for device in gpu_devices):
    print("SUCCESS: Metal acceleration is recognized.")
else:
    print("FAILURE: Metal plugin not found. TensorFlow is running on CPU only.")

# 3. Test a basic operation on the GPU
try:
    with tf.device('/GPU:0'):
        a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
        b = tf.constant([[1.0, 1.0], [0.0, 1.0]])
        c = tf.matmul(a, b)
        print("Metal Operation Test: SUCCESS")
except Exception as e:
    print(f"Metal Operation Test: FAILED with error: {e}")
