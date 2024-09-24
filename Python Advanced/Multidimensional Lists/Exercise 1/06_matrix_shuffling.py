rows, columns = [int(num) for num in input().split()]
matrix = [[char for char in input().split()]for row in range(rows)]
command = input().split()
while command[0] != "END":
    if command[0] != "swap" or len(command) != 5 or int(command[1]) > rows or int(command[2]) > columns or int(command[3]) > rows or int(command[4]) > columns:
        print("Invalid input!")
    else:
        temp_value = matrix[int(command[1])][int(command[2])]
        matrix[int(command[1])][int(command[2])] = matrix[int(command[3])][int(command[4])]
        matrix[int(command[3])][int(command[4])] = temp_value
        for row in range(rows):
            for col in range(columns):
                print(matrix[row][col], end=" ")
            print()
    command = input().split()