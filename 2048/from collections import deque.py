from collections import deque
import numpy as np
import g2048
import random
import time
# a=[]

gst=g2048.bot2048()
averscore=[]
# for i in range(100):
#     if len(a)>9:
#         a.pop(0)
#         a.append(i)
#     else:
#         a.append(i)
# print("%0.2f"%(np.average(a)))
score=0
while True:
    x_t1,terminal,r_0 = gst.move(random.randint(0,3))
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
    print('s:%d avs:%f'%(gst.score,np.average(averscore)))