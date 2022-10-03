import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
# 准备数据 
a = np.random.randint(95,100, (20, 2)).astype(np.float32) 
b = np.random.randint(90,95, (20, 2)).astype(np.float32) 
data = np.vstack((a, b)) 
data = np.array(data, dtype="float32") 
    
# 建立分组标签，0代表A级，1代表B级 
aLabel=np.zeros((20,1)) 
bLabel=np.ones((20,1)) 
label = np.vstack((aLabel, bLabel)) 
label = np.array(label, dtype="int32") 
    
# 训练 
svm = cv2.ml.SVM_create() 
# 属性设置，直接采用默认值即可 
#svm.setType(cv2.ml.SVM_C_SVC)    # svm type 
#svm.setKernel(cv2.ml.SVM_LINEAR) # line 
#svm.setC(0.01) 
result = svm.train(data, cv2.ml.ROW_SAMPLE, label) 
    
#预测 
test = np.vstack([[98,90], [90,99]]) 
test = np.array(test, dtype="float32") 
(p1, p2) = svm.predict(test)   # test 是 [[数据1],[数据2]] 结构的
   
# 结果 
print(test)
print("res1",p2[0])
print("res2",p2[1]) 
plt.scatter(a[:,0], a[:,1], 80, "g", "o") 
plt.scatter(b[:,0], b[:,1], 80, "b", "s") 
plt.scatter(test[:,0], test[:,1], 80, "r", "*") 
plt.show() 
