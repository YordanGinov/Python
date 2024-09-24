row_column_count = int(input())
matrix = []
for row in range(row_column_count):
    elements = input()
    matrix.append([el for el in elements])
symbol = input()
found = False

for row in range(row_column_count):
    for column in range(row_column_count):
        if matrix[row][column] == symbol:
            print(f"({row}, {column})")
            found = True
            break
    if found:
        break
if not found:
    print(f"{symbol} does not occur in the matrix")