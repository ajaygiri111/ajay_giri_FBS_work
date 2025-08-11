#2 WAP to print even number 1 to n
num= int(input("enter the number"))
i = 1
for i in range(i,num+1,):
    if(i % 2 == 0 ):
        print(i,end=' ')
    else:
        print("odd {i}")