import tensorflow as tf
from tensorflow import keras
from keras import layers,Sequential,optimizers,losses
import numpy as np
import random
import os

x_train = np.zeros((10000,3))
y_train = np.zeros((10000,5))
for i in range(10000):
    a=random.randint(1,2)
    b=random.randint(1,5)
    x=random.randint(1,5)
    c=-(a*(x**2)+b*x)
    # if (b**2-4*a*c)<0:
    #     result1=-100
    #     result2=-100
    
    
    
    x_train[i][0]=a
    x_train[i][1]=b
    x_train[i][2]=c
    y_train[i][x-1]=1



# x=tf.random.normal([10,3])
# out=network(x)

#network.summary()
network=Sequential([

layers.Dense(10,activation=None),
layers.ReLU(),
layers.Dense(5,activation=None)

])
network.build(input_shape=(1,3))
network.compile(optimizer=keras.optimizers.Adam(learning_rate=0.01),
loss=keras.losses.CategoricalCrossentropy(from_logits=True),
metrics=['accuracy'])
if os.path.exists(r'testnw\checkpoint'):
    
    network.load_weights(r'testnw\netw1145.ckpt')
    print('lodingggggggg---')

history=network.fit(x_train,y_train,epochs=10,validation_data=(x_train,y_train),validation_split=0.2)
network.save_weights(r'testnw\netw1145.ckpt')    
# while True:
#     a=int(input('a:'))
#     b=int(input('b:'))
#     c=int(input('c:'))
#     xtest=[[a,b,c]]
    
#     print('%dx^2+%dx%d=0'%(xtest[0][0],xtest[0][1],xtest[0][2]))
#     print(np.argmax(network.predict(xtest),axis=1)+1)

