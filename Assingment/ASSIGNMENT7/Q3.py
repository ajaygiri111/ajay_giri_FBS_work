# 1
# 1 2
# 1   3
# 1     4
# 1 2 3 4 5

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if(j == 1 or j == i or i == 5):
#          print(j, end=" ")
#         else:
#            print(" ", end=" ")
#     print()


for i in range(1, 6):
    for j in range(1, 7 - i ):
        if(i == 5 or i == j or i == 1):
         print(j, end=" ")
        else:
           print(" ", end=" ")
    print()