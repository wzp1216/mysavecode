from random import randint
from time import time,sleep
from multiprocessing import Process
from threading import Thread
import os

class Downtask(Thread):
    def __init__(self,filename):
        super().__init__()
        self.filename=filename
    def run(self):
        print("start download ",self.filename," ...")
        print("process id is  ",os.getpid()," ...")
        print("father process id is  ",os.getppid()," ...")
        time_to_down=randint(5,10)
        sleep(time_to_down)
        print('%s down ok , use %d sec \n' %(self.filename,time_to_down))


class downclass(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print("start download ",self.name," ...")
        print("process id is  ",os.getpid()," ...")
        print("father process id is  ",os.getppid()," ...")
        time_to_down=randint(5,10)
        sleep(time_to_down)
        print('%s down ok , use %d sec ' %(self.name,time_to_down))
        

def mutiprocess():
    start=time()
    p1=downclass('aaa')
    p2=downclass('bbb')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end=time()
    print('use time :',end-start)

def mutithread():
    start=time()
    p1=Downtask('aaaaaaaaaaaaaaa')
    p1.start()
    p2=Downtask('bbbbbbbbbbbbbbbb')
    p2.start()
    p1.join()
    p2.join()
    end=time()
    print('use time :',end-start)


if __name__=='__main__':
    print("this is the main\n\n\n")
    print('main pid:',os.getpid())
    print('main ppid:',os.getppid())
    
    mutiprocess()
    print("**************************************")
    mutithread()

    print("main is end !!!\n\n\n")





