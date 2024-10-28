def yield_test(n):
    for i in range(n):
        yield i*2
        print("i=",i)
    print("this is end")

for i in yield_test(5):
    print(i,",")

