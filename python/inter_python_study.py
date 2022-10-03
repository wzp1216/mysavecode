'''
alist=[1,2,3,4,5]
b=[x*x for x in alist]
print(b)


mytuple=("aa",8,3,3)
print(mytuple)
print(mytuple.index(8))

mylist=list(mytuple)
print(mylist)  

'''

from collections import Counter
a="aaaaaaaaaadlskdjf;ajjj"
cc=Counter(a)
print(a)
print(list(cc.elements()))