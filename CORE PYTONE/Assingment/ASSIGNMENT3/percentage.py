# Input 5 subject marks from user and display grade(eg.First class,Second class ..)
sub1 =int(input("enter the marks of sub1"))
sub2 =int(input("enter the marks of sub2"))
sub3 =int(input("enter the marks of sub3"))
sub4 =int(input("enter the marks of sub4"))
sub5 =int(input("enter the marks of sub5"))

percentage_grade =(sub1+sub2+sub3+sub4+sub5) / 5


if(percentage_grade>=95):
    print(f'A+ grade')

elif(percentage_grade>=90):
    print(f'B+ grade')

elif(percentage_grade>=80):
    print(f'B grade')

elif(percentage_grade>=60):
    print(f'C grade')

elif(percentage_grade>=50):
    print(f'D grade')

else:
    print(f'student is fail')

   