myfile=open('myfile.txt','a')
myfile.write('hello text file\n')
myfile.close()


myfile=open('myfile.txt')
for line in myfile:
    print(":--",line,end='')




