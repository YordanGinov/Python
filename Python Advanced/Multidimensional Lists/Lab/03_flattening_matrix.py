row = int(input())
matrix = []

for i in range(row):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

matrix_list = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i]))]
print(matrix_list)
