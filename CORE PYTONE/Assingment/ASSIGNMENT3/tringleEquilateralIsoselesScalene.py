angle1 = int(input("enter the angle"))
angle2 = int(input("enter the angle"))
angle3 = int(input("enter the angle"))

if(angle1==angle2==angle3):
    print(f'angale is equilater')
elif(angle1==angle2):
    print(f'angale is isosceles')
elif(angle1!=angle2!=angle3):
     print(f'angale is Scalene')
else:
    print(f'angale is not any type tringle')