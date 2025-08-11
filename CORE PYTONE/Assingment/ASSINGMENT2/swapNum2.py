x = int(input('enter the value of x'))
y = int(input('enter the value of y'))

x = x + y 
y = x - y
x = x - y 
 
print(f'x:{x}, y:{y}')

# python shortcut
x = int(input('enter the value of x'))
y = int(input('enter the value of y'))
 
x,y = y,x

print(f'x:{x}, y:{y}')