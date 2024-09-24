row_count, column_count = [int(el) for el in input().split()]
matrix = [[int(c) for c in input().split()]for row in range(row_count)]
highest_sum = -181
sub_matrix = []
for row in range(row_count-2):
    for col in range(column_count-2):
        current_sum = 0
        current_matrix = []
        for i in range(row, row + 3):
            current_matrix.append([])
            for j in range(col, col + 3):
                current_sum += matrix[i][j]
                current_matrix[i - row].append(matrix[i][j])
        if current_sum > highest_sum:
            highest_sum = current_sum
            sub_matrix = current_matrix
print(f"Sum = {highest_sum}")
for row in range(len(sub_matrix)):
    for col in range(len(sub_matrix[row])):
        print(sub_matrix[row][col], end=" ")
    print()
