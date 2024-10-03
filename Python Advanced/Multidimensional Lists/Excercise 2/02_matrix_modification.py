rows_columns = int(input())
matrix = [[int(num) for num in input().split()] for row in range(rows_columns)]
command = input().split()
while command[0] != 'END':
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if row >= rows_columns or col >= rows_columns or row < 0 or col < 0 or (command[0] != "Add" and command[0] != "Subtract"):
        print("Invalid coordinates")
    elif command[0] == "Add":
        matrix[row][col] += value
    elif command[0] == "Subtract":
        matrix[row][col] -= value
    command = input().split()
for row in range(rows_columns):
    for col in range(rows_columns):
        print(matrix[row][col], end=" ")
    print()