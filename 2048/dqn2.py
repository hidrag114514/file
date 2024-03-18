import tensorflow as tf
from tensorflow import keras
from keras import layers,Sequential,optimizers,losses
import numpy as np
import random
import os
import g2048 as game
from collections import deque


# x_train = np.zeros((10000,3))
# y_train = np.zeros((10000,5))
# for i in range(10000):
#     a=random.randint(1,2)
#     b=random.randint(1,5)
#     x=random.randint(1,5)
#     c=-(a*(x**2)+b*x)
#     # if (b**2-4*a*c)<0:
#     #     result1=-100
#     #     result2=-100
    
    
    
#     x_train[i][0]=a
#     x_train[i][1]=b
#     x_train[i][2]=c
#     y_train[i][x-1]=1



# x=tf.random.normal([10,3])
# out=network(x)

#network.summary()
network=Sequential([

layers.Dense(20,activation=None,),
layers.ReLU(),
layers.Dense(10,activation=None),
layers.ReLU(),
layers.Dense(4,activation='linear')
])
network.build(input_shape=(1,16))
network.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001),
loss='mse')
if os.path.exists(r'dqnnw\checkpoint'):
#if os.path.exists(r'dqnn\model.h5'):
    network.load_weights(r'dqnnw\netw1145.ckpt')
    #network=keras.models.load_model(r'dqnn\model.h5')
    print('lodingggggggg---')
observe=1000
i=0
epsilon=0.02
# history=network.fit(x_train,y_train,epochs=10,validation_data=(x_train,y_train),validation_split=0.2)
# network.save_weights(r'testnw\netw1145.ckpt')   
gst=game.bot2048()
memory=deque(maxlen=observe)
averscore=[]
# x=np.zeros((observe,16))
# y=np.zeros((observe,4))

do_nothing = np.zeros(4)
do_nothing[0] = 1
x_t,terminal,r_0 = gst.move(np.argmax(do_nothing)) 
s_t = np.array(x_t)
s_t=s_t.reshape(1,16)/12
rept=0
action_index = 0
score=0
while True:
    # x_t,terminal,r_0 = gst.move(np.argmax(network.predict(s_t)))
    # s_t = np.array(x_t)
    # s_t=s_t.reshape(16)
    if i>observe:
        #history=network.fit(x,y,epochs=1)
        # i=0
        # x=np.zeros((observe,16))
        # y=np.zeros((observe,4))
        
        
        minibatch=random.sample(memory,5)
        for s,a,r,s1,terminal in minibatch:
            target=r
            if terminal:
                target=r+0.9*np.argmax(network.predict(s1.reshape(1,16),verbose=0))
            target_f=network.predict(s.reshape(1,16),verbose=0)
            target_f[0][np.argmax(a)]=target
            network.fit(s.reshape(1,16),target_f,epochs=1,verbose=0)
        
        
        if i%500==0:
            #network.save(r'dqnn\model.h5')
            network.save_weights(r'dqnnw\netw1145.ckpt')
            print('savinggggg-----------')
        
    
    a_t = np.zeros(4)
    #action_index = 0
    
    if random.random() <= epsilon:
        print("----------Random Action----------")
        
        a_t[random.randrange(4)] = 1
        if epsilon!=1e-4:
            epsilon-=1e-5
    else:
        resu=network.predict(s_t,verbose=0)
        if action_index==np.argmax(resu):
            rept+=1
        else:
            rept=0
        if rept>=5:
            print("----------protRandom Action----------")
            action_index = random.randrange(4)
            # if action_index!=np.argmax(resu):
            #     rept=0
        else:
            action_index = np.argmax(resu)
        a_t[action_index] = 1

    x_t1,terminal,r_0 = gst.move(action_index)
    s_t1 = np.array(x_t1)
    s_t1=s_t1.reshape(1,16)/12
    memory.append((s_t.reshape(16),a_t,r_0,s_t1.reshape(16),terminal))
    #x[i]=s_t.reshape(16)
    if not terminal:
        if len(averscore)>9:
            averscore.pop(0)
            averscore.append(score)
        else:
            averscore.append(score)
        #averscore.append(score)
        score=gst.score
    else:
        score=gst.score
    print('score:%d   a:%d  r:%d ascore:%f'%(gst.score,action_index,r_0,np.average(averscore)))
    
    
    s_t=s_t1
    i=i+1
# print(x)
# print(y)
# x=np.array([[1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
# # print(network.predict(x[0]))
# y=np.array([[ 0,0, 0,-9.84068395],
#  [ 0,0, 0,-9.84068395],
#  [ 0,0, 0,-9.84068395],
#  [ 0,0, 0,-9.84068395],
#  [ 0,0, 0,-9.84068395]])

# history=network.fit(x,y,epochs=2,validation_data=(x,y),validation_split=0.2)