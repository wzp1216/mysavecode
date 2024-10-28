from datetime import date
import zlib
import sys

def testdate():
    now=date.today()
    print(now)
    birthday=date(1978,12,1)
    days=now-birthday
    age=now.year-birthday.year
    print("days is :",days)
    print("age is :",age)

def testzip():
    m=b'This is a test compress'
    print(m)
    print("len of m is ",len(m))

    t=zlib.compress(m)
    print(t)
    print("len of t is ",len(t))

    s=zlib.decompress(t);
    print(t)



def testsys():
    print(sys.path)




#testdate()
#testzip()
testsys()
