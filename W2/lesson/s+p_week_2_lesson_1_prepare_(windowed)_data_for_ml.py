# -*- coding: utf-8 -*-
"""S+P Week 2 Lesson 1 - Prepare (Windowed) Data for ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11xJuxRSCHQCSvTEVLcQCFScLkhMhdDTt
"""

#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Commented out IPython magic to ensure Python compatibility.
try:
  # %tensorflow_version only exists in Colab.
#   %tensorflow_version 2.x
except Exception:
  pass

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import sys
print(sys.version)
print(tf.__version__)

dataset = tf.data.Dataset.range(10)
for val in dataset:
   print(val.numpy())

dataset = tf.data.Dataset.range(10)
dataset = dataset.window(5, shift=1) # create a window of size 5
for window_dataset in dataset:
  for val in window_dataset:
    print(val.numpy(), end=" ")
  print()

dataset = tf.data.Dataset.range(10)
dataset = dataset.window(5, shift=1, drop_remainder=True)
for window_dataset in dataset:
  for val in window_dataset:
    print(val.numpy(), end=" ")
  print()

dataset = tf.data.Dataset.range(10)
dataset = dataset.window(5, shift=1, drop_remainder=True)
dataset = dataset.flat_map(lambda window: window.batch(5))
for window in dataset:
  print(window.numpy())

dataset = tf.data.Dataset.range(10)
dataset = dataset.window(5, shift=1, drop_remainder=True)
dataset = dataset.flat_map(lambda window: window.batch(5))
dataset = dataset.map(lambda window: (window[:-1], window[-1:]))
for x,y in dataset:
  print(x.numpy(), y.numpy())

dataset = tf.data.Dataset.range(10)
dataset = dataset.window(5, shift=1, drop_remainder=True)
dataset = dataset.flat_map(lambda window: window.batch(5))
dataset = dataset.map(lambda window: (window[:-1], window[-1:]))
dataset = dataset.shuffle(buffer_size=10) # to ensure no sequence bias 
for x,y in dataset:
  print(x.numpy(), y.numpy())

dataset = tf.data.Dataset.range(10)
dataset = dataset.window(5, shift=1, drop_remainder=True) # window size 5, 
                                                          # shift 1 at a time, 
                                                          # drop_remainder ensures each contains 5 elements
dataset = dataset.flat_map(lambda window: window.batch(5))
dataset = dataset.map(lambda window: (window[:-1], window[-1:]))
dataset = dataset.shuffle(buffer_size=10)
dataset = dataset.batch(2).prefetch(1) # each batch contains 2 entries 
for x,y in dataset:
  print("x = ", x.numpy())
  print("y = ", y.numpy())