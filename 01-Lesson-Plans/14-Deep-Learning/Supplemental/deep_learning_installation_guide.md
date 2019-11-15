# Deep Learning Setup Guide

This guide serves as a step by step process for setting up and validating the tools required for the deep learning portion of the curriculum.

This guide will include installation and verification steps for the following technologies:

* [TensorFlow 2.0](#TensorFlow)

* [Keras](#Keras)

---

## TensorFlow

### Install

The `TensorFlow 2.0` package has several dependencies which should already be installed in the default conda environment. Please refer to the [troubleshooting](#Troubleshooting) section for details about this environment. Make sure to run the following commands with your conda environment activated.

Open the terminal, and execute the following command to install `TensorFlow`.

* Use the `pip install` command to install the `TensorFlow 2.0` module.

```shell
pip install --upgrade tensorflow
```

### Verify Installation

Once the `TensorFlow` install is complete, verify the installation completed successfully.

```shell
python -c "import tensorflow as tf;print(tf.__version__)"
```

The output of this command should show version `2.0.0` or higher.

---

## Keras

Keras is a popular deep learning framework that serves as a high-level API for TensorFlow. Keras is now included with TensorFlow 2.0, so run the following commnand to verify that the package is available:

```shell
python -c "import tensorflow as tf;print(tf.keras.__version__)"
```

The output should be `2.2.4-tf` or later.

---

## Troubleshooting

It can be frustrating when packages do not install correctly. Refer to the latest official [TensorFlow Install Guide](https://www.tensorflow.org/install/pip) to troubleshoot.

You can also use [Google Colaboratory](https://colab.research.google.com/) with TensorFlow.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
