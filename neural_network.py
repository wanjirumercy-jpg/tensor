# -*- coding: utf-8 -*-
"""Neural Network

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Gq-2lqi9zosVeu3xS54Vk4Bu2RCmrRWU

Import the Required Libraries
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout,Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

"""Load and Preprocess Data"""

#Load mnist dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Normalize the images to a range of 0 to 1
x_train, x_test = x_train / 255.0, x_test / 255.0

#One-hot encode the labels
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

"""Define the Model architecture"""

model = Sequential()

#Flatten the input data (28x28 to 1D)
model.add(Flatten(input_shape=(28, 28)))

#Add a dense layer with 128 units and ReLU activation
model.add(Dense(128, activation='relu'))

#Add a dropout layer to prevent overfitting
model.add(Dropout(0.2))

#Add another dense layer with 32 units and ReLU activation
model.add(Dense(32, activation='relu'))

#Output layer with 10 neurons (one for each digit) and softmax activation
model.add(Dense(10, activation='softmax'))

"""Compile the model"""

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

"""Train the Model"""

model.fit(x_train, y_train, epochs=10, batch_size=32)

"""Evaluate the Model"""

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc}')

"""Model predictions"""

predictions = model.predict(x_test)
print(f"Predicted label for the first image: {tf.argmax(predictions[0]).numpy()}")
print(f"True label for the first image: {tf.argmax(y_test[0]).numpy()}")

predictions = model.predict(x_test)
print(f"Predicted label for the third image: {tf.argmax(predictions[2]).numpy()}")
print(f"True label for the third image: {tf.argmax(y_test[2]).numpy()}")

predictions = model.predict(x_test)
print(f"Predicted label for the fith image: {tf.argmax(predictions[5]).numpy()}")
print(f"True label for the fifth image: {tf.argmax(y_test[5]).numpy()}")

predictions = model.predict(x_test)
print(f"Predicted label for the seventh image: {tf.argmax(predictions[6]).numpy()}")
print(f"True label for the seventh image: {tf.argmax(y_test[6]).numpy()}")