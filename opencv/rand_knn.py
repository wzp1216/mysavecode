import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

traindata=np.random.randint(0,100,(15,2)).astype(np.float32)
responses=np.random.randint(0,2,(15,1)).astype(np.float32)

red=traindata[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')
print(red)

blue=traindata[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')
print(blue)

plt.show()


newcomer=np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

knn=cv.KNearest()
knn.train(traindata,responses)
res,results,neighbours,dist=knn.find_nearest(newcomer,3)

plt.show()
