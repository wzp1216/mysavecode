def testint():
    while True:
        try:
            x=int(input("please input a int number:"))
            break
        except ValueError:
            print("That was no valid number. Try again...")
    return x


if __name__=='__main__':
   x=testint()
   print(x)


