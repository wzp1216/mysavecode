
def deposit():
    while True:
        amount=input("please iput deposit $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("iput must>0")
        else:
            print("please input a number!")
    return amount

print(deposit())

