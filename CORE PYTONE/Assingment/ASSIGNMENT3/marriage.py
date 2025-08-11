gender = str(input("enter the gender(M/F):"))
age = int(input("enter the age"))

if((gender == 'M' and age>=21) or (gender == 'F' and age>=18 )):
    print('eligible for marriage')
else:
    print("not eligible fo marriage")