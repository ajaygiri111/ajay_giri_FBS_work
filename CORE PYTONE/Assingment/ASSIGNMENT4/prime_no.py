# # WAP to print prime number
# num = int(input("enter the number"))
# for i in range (2,num//2):
#     if(num % i == 0):
#         print(f'{num} is not prime number')
#         break
# else:
#     print(f'{num} is prime number')
    



# WAP to primt prime number to we need to all prime
n = int(input("enter the number"))
count = 0 
num = 2
while(count < n):
    for i in range(2,num // 2 + 1):
        if(num % i==0):
            break
    else:
     print(num,",", end=" ")
    
    num+=1
    count+=1
print(F'this is first {n} prime number')


        
