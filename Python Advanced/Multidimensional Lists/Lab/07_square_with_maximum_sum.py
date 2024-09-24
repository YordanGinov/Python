from sys import maxsize
rows, columns = [int(el) for el in input().split(", ")]
matrix = []
highest_sum = -maxsize
sub_matrix = []
for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)

for row in range(rows - 1):
    for col in range(columns - 1):
        current_sum = matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1]
        if current_sum > highest_sum:
            highest_sum = current_sum
            sub_matrix=[[matrix[row][col], matrix[row][col+1]],[matrix[row+1][col], matrix[row+1][col+1]]]
sub_matrix_list = [sub_matrix[el] for el in range(len(sub_matrix))]
print(*sub_matrix_list[0])
print(*sub_matrix_list[1])
print(highest_sum)