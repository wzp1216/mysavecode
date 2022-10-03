import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time


#生成模拟数据
a=np.random.randint(95,100,(20,2)).astype(np.float32)
b=np.random.randint(90,95,(20,2)).astype(np.float32)
data=np.vstack((a,b))
data=np.array(data,dtype='float32')

#构造分组标签
alabel=np.zeros((20,1))
blabel=np.ones((20,1))
label=np.vstack((alabel,blabel))
label=np.array(label,dtype='int32')

#训练

svm=cv.ml.SVM_create()
#svm.setType(cv.ml.SVM_C_SVC)

result=svm.train(data,cv.ml.ROW_SAMPLE,label)

#分类
test=np.vstack([[98,90],[90,99]])
test=np.array(test,dtype='float32')

(p1,p2)=svm.predict(test)

#显示分类结果
plt.scatter(a[:,0],a[:,1],80,'g','o')
plt.scatter(b[:,0],b[:,1],80,'b','s')
plt.scatter(test[:,0],test[:,1],80,'r','*')
plt.show()

print("test is:",test)
print("p2 is :",p2)

