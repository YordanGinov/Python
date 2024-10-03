user_input = input().split("|")
matrix = [[el for el in row.split()] for row in user_input]
for row in range(len(matrix) - 1, -1, -1):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=" ")