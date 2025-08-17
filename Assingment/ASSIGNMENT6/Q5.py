#           * 
#         * * * 
#       * * * * *    
#     * * * * * * *  
#   * * * * * * * * *
        
# rows = 5  # number of rows

# for i in range(1, rows + 1):
#     # print leading spaces
#     for j in range(1, rows - i + 1):
#         print(" ", end=" ")

#     # print stars (2*i - 1 stars in each row)
#     for j in range(1, 2 * i):
#         print("*", end=" ")

#     # move to next line
#     print()




#           * 
#         * * * 
#       * * * * *    
#     * * * * * * *  
#   * * * * * * * * *

for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for j in range(1, 2 * i ):
        print("*", end=" ")
    print()