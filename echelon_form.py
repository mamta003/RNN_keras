
# r1, r2 = mat
# print(mat[0])

# for j in range(0,2,1):
#         for i in range(0,2,1):
#                 r1 = [x/mat[0][0] for x in r1]
#                 r2 = [(y-(1*3)) for y in r2]
            #     r1 = mat[0][j]/5  
#               mat[i][j] = mat[i][j]/mat[i][0]
# print(r1)            
# print(r2)
# interchange row 
# # A[i], A[j] = A[j], A[i]
# i = 2
# j = 2
# c = 3

# A = [[1,2,3,4],[4,5,6,4],[7,8,9,4],[5,3,8,9]]

# row_op(matrix, constant to be multiplied, row to be changed, row to be used to change)
def row_op(A,i,j):
    # for m in range(0,len(A[0])):
        for k in range(0,len(A[0])):
            A[i][k] = A[i][k] - (A[j][k])
        return A
# print(row_op(A,1,0))
# col_op(matrix, constant to be multiplied, col to be changed, col to be used to change)
def col_op(A,c,i,j):
    for k in range(0,len(A[0])):
       A[k][i] = A[k][i] - A[k][j]
    return A

# exchange rows --> xchange(matrix, row 1 for interchange, row 2 for interchange)

import numpy as np




        # print[x]
        # while x != 0:
        # x = A[n]/-2
        # else:
        #     print("its a row row")
    
    # data[x][y] = data[x][y]/data[x][0]

# def echelon_form(A):
    # a_11, a_12 = input("Enter first row of 2x2 matrix").split()
    # a_21, a_22 = input("Enter second row of 2x2 matrix").split()
    # A = [[a_11, a_12], [a_21, a_22]]
    # for i in range(0,len(A[0])):
    #     for ele in A[i]:
    #         if ele != 0:
    #             break
    #     B = make1(A)
    # print("B=",B)
    
    # print(B)
    # B= [[1,2],[3,4]]
    # for k in range(1,len(A[0])+1):
# for i in range(1,len(A[0]),1):
            # for j in range(0,len(A[0])):
    # for j in range(0,len(A[0])):
            # i == 1
        # C = row_op(B,i,0)
        # D = np.delete(C,0,0)
        # for i in range(0,len(A[0])-1):
            # for j in range(0,len(A[0])):
                # no_zero = np.delete(D[i]==0.0)
                
                # D[i] = D.pop(0)

        # A = D
        # return D
    # print("C=",C)
    # print("D=",D)
    # print("A=",A)
            # i += 1
    

            # for ele in A[i]:
                # if A[i][j] != 0:
                    # c = A[i][j]
                    
                    # C = row_op(B,1,0)
                    
    # else:
        # print("not in range")
    # print(mat)

    # print(C)

# mat = xchange(mat,0,1)
# a_11 = int(input("Enter first row of 2x2 matrix"))
# a_12 = int(input("Enter first row of 2x2 matrix"))
# a_21 = int(input("Enter second row of 2x2 matrix"))
# a_22 = int(input("Enter second row of 2x2 matrix"))
# A = [[a_11, a_12], [a_21, a_22]]
# print(echelon_form(A))
# B= [[1,2],[3,4]]
# # for k in range(1,len(A[0])+1):
#     # for i in range(k,len(A[0]),1):
#         # for j in range(0,len(A[0])):
# C = row_op(B,1,0)
# print(C)
import numpy as np
def make1(A,m):
    B = np.zeros([len(A),len(A)])
    for i in range(len(A)):
         -0.0 == +0.0 == 0.0
         for j in range(len(A)):
            B[i][j] += A[i][j]/A[i][m]
    return B
import numpy as np

A = [[0, 0, 0],[0, 0, 0], [0, 3, 9], [4, 5, 6]]
def xchange(A, i, j):
    A[i], A[j] = A[j], A[i]
    return A
# print(xchange(A,0,1))

def echelon(A):
    # col = 0
    # for i in range(0,len(A)):
    # while (col < len(A)):
    #     # for i in range(0,len(A)):
    #         max_col = max([ele for i in range(0,len(A)) for ele in A[i][col]])
    #         col += 1
    #         return max_col
    
#     # B = np.zeros([len(A),len(A)])
#     # C = np.zeros([len(A),len(A)])
#     row, col = A.shape

    row = 0
    col = 0
    
    while all([ele == 0 for ele in A[row]]):
        # for i in range(1,len(A)):
            xchange(A,row,len(A)-1)
            row += 1
        
    
    while  (A[row][col] == 0):
        col += 1
    
    # for ele in range(row,len(A)):
    # while row < (len(A)): 
    while (row< len(A) and col < len(A)):  
        a = A[row][col]
        # for j in range(col,len(A)):
            # A[row][j] = A[row][j]/a
        # col += 1
        row += 1
    return A
print(echelon(A))
# B = echelon(A)
# print(B[0][0])
    
    
#     for i in range(0,len(A)):
#         for j in range(len(A)):
#             # for ele in A[row]:
               
#     return (row,col)
# print(find_row(A))
# print(find_row(A),find_col(A,0))
# print(find_col(A,find_row(A)))




        

   
    # return row,col    
    
            # B = make1(A,col)
            # C[i][j] = B[row+i][j] - B[row][j]

    
                
            # A[0][j] = A[0][j]/A[0][j]
    # print(row,col)
# print(make1(A,1))
# print(echelon(A))

'''fromm google'''
# A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# def gauss_elimination(A):
#     row, col = A.shape
#     if row == 0 or col == 0:
#         return A
#     for i in range(min(row, col)):
#         max_element = abs(A[i, i])
#         max_row = i
#         for k in range(i+1, row):
#             if abs(A[k, i]) > max_element:
#                 max_element = abs(A[k, i])
#                 max_row = k
#         A[[i, max_row]] = A[[max_row, i]]
#         for k in range(i+1, row):
#             factor = A[k, i]/A[i, i]
#             A[k, :] -= factor * A[i, :]
#     return A
# print(gauss_elimination(A))

# def echelon(A):
#     row = 0
#     # for ele in A[row]:
#     while [ele == 0 for ele in A[]] == 0:
#             row+=1
#         return row
#     return row
# print(echelon(A))