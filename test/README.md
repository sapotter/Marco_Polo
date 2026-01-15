# README For The `test` Directory

See: [TensorFlow Guide](https://www.tensorflow.org/guide)

This directory contains test files for the project. 

## Running TensorFlowMNist.py

To run TensorFlowMNist.py, activate environment `polo0.2.1` and install `tensorflow_datasets` with Pip:

```bash
pip install tensorflow_datasets
```

Run TensorFlowMNist.py with:

```bash
python TensorFlowMNist.py
```

>**NOTE** `EagerCpuGpuConfig.py` script which contains a class to make the GPU visible or invisible to ML computations. It is required to run `TensorFlowMNist.py` and must be in the same directory as `TensorFlowMNist.py`. 

As a “Hello World” test of TensorFlow, use the MNIST problem. It is part of the tensorflow_datasets that was installed. It is a group of raster pictures of handwritten digits from 0 to 9. The goal is to categorize and then recognize them.

The TensorFlowMNistTest.py code splits the MNIST data into train and test data. Then, it builds a tensorflow keras model and compiles it. Lastly, it performs 12 epochs of \[fitting the model to the test data and validation\] ending up with 99.07% validation accuracy. This means that, theoretically, there is also a 99.07% probability that in inference, the next received digit will be mapped to the correct category from 0 to 9.


See [Visualizing MNIST: An Exploration of Dimensionality Reduction](http://colah.github.io/posts/2014-10-Visualizing-MNIST/) for visual as well as full mathematical explanation of this problem and its solution method