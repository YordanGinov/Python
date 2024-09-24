row_count, column_count = [int(el) for el in input().split()]
matrix = [[c for c in input().split()]for row in range(row_count)]
count = 0
# for row in range(row_count):
#     elements = [el for el in input().split()]
#     matrix.append(elements)

for row in range(row_count -1):
    for col in range(column_count -1):
        if matrix[row][col] == matrix[row][col+1] and matrix[row][col] == matrix[row+1][col] and matrix[row+1][col] == matrix[row+1][col+1]:
            count +=1
print(count)