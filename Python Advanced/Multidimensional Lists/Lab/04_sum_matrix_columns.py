rows_count, columns_count = [int(el) for el in input().split(", ")]
matrix = []

for row in range(rows_count):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for column in range(columns_count):
    column_sum = 0
    for row in range(rows_count):
        column_sum += matrix[row][column]
    print(column_sum)
