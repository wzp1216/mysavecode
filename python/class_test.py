# clock class;
# init; go; show;

import time

class clock(object):
    def __init__(self,hour=0,minute=0,sec=0):
        self.hour=hour
        self.minute=minute
        self.sec=sec
    def go(self):
        self.sec=self.sec+1;
        if self.sec==60:
            self.minute+=1
            self.sec=0
        if self.minute==60:
            self.hour+=1
            self.minute=0
        if self.hour==24:
            self.hour,self.minute,self.sec=0,0,0
    def show(self):
        return("--%02d:%02d:%02d--"%(self.hour,self.minute,self.sec))
if __name__=='__main__':
    myclock=clock(23,59,58)
    while True:
        print(myclock.show())
        time.sleep(0.1)
        myclock.go()

