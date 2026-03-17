# Addition of two matrices
A = []
B = []
C = []
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
print("Enter elements of first matrix:")
for i in range(r):
    row = []
    for j in range(c):
        val = int(input())
        row.append(val)
    A.append(row)
print("Enter elements of second matrix:")
for i in range(r):
    row = []
    for j in range(c):
        val = int(input())
        row.append(val)
    B.append(row)
# Addition
for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print("Addition of matrices is:")
for i in range(r):
    for j in range(c):
        print(C[i][j], end=" ")
    print()