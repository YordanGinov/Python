m_size = int(input())
commands = input().split()
coal_amount = 0
matrix = [[] for row in range(m_size)]
miner_row = -1
miner_col = -1
end_of_route_row = -1
end_of_route_col = -1
for row in range(m_size):
    row_data = input().split()
    for element in range(len(row_data)):
        if row_data[element] == "c":
            coal_amount += 1
        elif row_data[element] == "s":
            miner_col = element
            miner_row = row
        elif row_data[element] == "e":
            end_of_route_col = element
            end_of_route_row = row
    matrix[row] = row_data
for command in commands:
    if command == "left":
        if miner_col - 1 >= 0:
            miner_col -= 1
    elif command == "right":
        if miner_col + 1 < m_size:
            miner_col += 1
    elif command == "up":
        if miner_row - 1 >= 0:
            miner_row -= 1
    elif command == "down":
        if miner_row + 1 < m_size:
            miner_row += 1
    if matrix[miner_row][miner_col] == "c":
        coal_amount -= 1
        matrix[miner_row][miner_col] = "*"
        if coal_amount <= 0:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            exit()
    elif matrix[miner_row][miner_col] == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        exit()
print(f"{coal_amount} pieces of coal left. ({miner_row}, {miner_col})")
