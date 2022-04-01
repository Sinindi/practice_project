"""
필요한 모듈 및 프레임워크를 잘 생각하고 넣자
"""
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint, EarlyStopping
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf
import numpy as np
import pandas as pd 
import os

"""
일반적인 학습 모델은 출력 갯수의 한계가 있음을 알았다.
이번엔 오토인코더를 이용한 모델을 구성해 볼 생각이다
입력값은 레이놀즈 수와 이미지의 합(바이너리가 아닌 회색)
출력은 타겟 이미지
"""
#[:,:196608]인풋 이미지,[:,196608:393216]레이놀즈수,[:,393216:]타겟 이미지
dataset = np.load('test3.npy', allow_pickle=True)
X = dataset[:,196608:393216]
Y = dataset[:,393216:]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state =1)
X_test, X_val,Y_test, Y_val = train_test_split(X_test,Y_test,test_size=0.5,random_state=1)
X_train = X_train.reshape(X_train.shape[0], 256,256,3)
X_test = X_test.reshape(X_test.shape[0], 256,256,3)
X_val = X_val.reshape(X_val.shape[0], 256,256,3)
Y_train = Y_train.reshape(Y_train.shape[0], 256,256,3)
Y_test = Y_test.reshape(Y_test.shape[0], 256,256,3)
Y_val = Y_val.reshape(Y_val.shape[0], 256,256,3)

tf.random.set_seed(44)

RI_inputs = keras.Input(shape = (256,256,3), name = 'RI_input')

Con1 = layers.Conv2D(16, 3, activation = 'elu', padding = 'same')(RI_inputs)
Max1 = tf.keras.layers.MaxPool2D(pool_size=(2))(Con1)

Con2= layers.Conv2D(32, 3, activation = 'elu', padding = 'same')(Max1)
#x = tf.keras.layers.BatchNormalization()(x)
Max2 = tf.keras.layers.MaxPool2D(pool_size=(2))(Con2)

Con3 = layers.Conv2D(64, 3, activation = 'elu', padding = 'same')(Max2)
#x = tf.keras.layers.BatchNormalization()(x)
Max3 = tf.keras.layers.MaxPool2D(pool_size=(2))(Con3)

Con4 = layers.Conv2D(128, 3, activation = 'elu', padding = 'same')(Max3)
#x = tf.keras.layers.BatchNormalization()(x)
Max4 = tf.keras.layers.MaxPool2D(pool_size=(2))(Con4)

Con5 = layers.Conv2D(256, 3, activation = 'elu', padding = 'same')(Max4)
#x = tf.keras.layers.BatchNormalization()(x)
Max5 = tf.keras.layers.MaxPool2D(pool_size=(2))(Con5)

Con6 = layers.Conv2D(512, 3, activation = 'elu', padding = 'same')(Max5)

ConT1 = layers.Conv2DTranspose(256, 3, activation = 'elu', padding = 'same')(Con6)
Up1= layers.UpSampling2D((2,2))(ConT1)

ConT2 = layers.Conv2DTranspose(128, 3, activation = 'elu', padding = 'same')(Up1)
Up2 = layers.UpSampling2D((2,2))(ConT2)

ConT3 = layers.Conv2DTranspose(64, 3, activation = 'elu', padding = 'same')(Up2)
Up3 = layers.UpSampling2D((2,2))(ConT3)

ConT4 = layers.Conv2DTranspose(32, 3, activation = 'elu', padding = 'same')(Up3)
Up4 = layers.UpSampling2D((2,2))(ConT4)

ConT5 = layers.Conv2DTranspose(3, 3, activation = 'elu', padding = 'same')(Up4)
Up5 = layers.UpSampling2D((2,2))(ConT5)

#outputs = layers.Dense(1)(x)

model = keras.Model(RI_inputs, Up5, name = 'resnet')

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0012, decay = 0.013),loss='mse', metrics=['mae'])

history = model.fit(X_train,Y_train,epochs=30, validation_data=(X_val, Y_val), batch_size=10)

#hist = model.fit(X_tr,Y_tr['M'],epochs=500, validation_data=(X_vid, Y_vid['M']), batch_size=32, callbacks = [callbacks,checkpoint])
#model.load_weights(modelpath)

model.summary()