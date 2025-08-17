# WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.

salary = float(input("enter basic salary"))

da = (salary*0.10)
ta = (salary*0.12)
hra = (salary*0.15)

print(f'da:{da},ta:{ta},hra:{hra}')

total_salary = (salary + da + ta + hra)

print(f'total_salary:{total_salary}')