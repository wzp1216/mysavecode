from time import sleep
from threading import Thread

class Account(object):
    def __init__(self):
        self._balance=0
    def deposit(sef,money):
        new_balance= self._balance+money
        sleep(0.01)
        self._balance=new_balance
    @property
    def balance(self):
        return self._balance

class AddmoneyThread(Thread):
    def __init__(self,account,money):
        super().__init__()
        self._account=account
        self.money=money
    def run(self):
        self._account.deposit(self.money)

def adderror():
    account=Account()
    threads=[]
    for _ in range(10):
        t=AddmoneyThread(account,1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print('The account money is ',account.balance)

if __name__=='__main__':
    adderror()

