row_count = int(input())
matrix = []
primary_diagonal_sum = 0
for row in range(row_count):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for row in range(row_count):
    primary_diagonal_sum += matrix[row][row]

print(primary_diagonal_sum)