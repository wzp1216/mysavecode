import pickle

class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show(self):
        print("name: ",self.name,"  ","age: ",self.age)

aa=person("wang",23)
print("this is out aa")
aa.show()

f=open('./pick.data','wb')
pickle.dump(aa,f)
f.close()

f=open('./pick.data','rb')
bb=pickle.load(f)
f.close()
print("this is out bb")
bb.show()

