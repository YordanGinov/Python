rows_cols = int(input())
matrix = [[int(el) for el in input().split()] for row in range(rows_cols)]
bombs = [el for el in input().split()]
active_cells = 0
active_cells_sum = 0

for bomb in bombs:
    row_bomb, col_bomb = [int(el) for el in bomb.split(",")]
    damage = matrix[row_bomb][col_bomb]
    if damage > 0:
        if row_bomb == 0:
            start_row = row_bomb
        else:
            start_row = row_bomb - 1
        if col_bomb == 0:
            start_col = col_bomb
        else:
            start_col = col_bomb - 1
        if row_bomb + 1 == rows_cols:
            end_row = row_bomb
        else:
            end_row = row_bomb + 1
        if col_bomb + 1 == rows_cols:
            end_col = col_bomb
        else:
            end_col = col_bomb + 1
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                if matrix[row][col] > 0:
                    matrix[row][col] -= damage
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] > 0:
            active_cells += 1
            active_cells_sum += matrix[row][col]
print(f"Alive cells: {active_cells}")
print(f"Sum: {active_cells_sum}")
for row in matrix:
    print(" ".join([str(el) for el in row]))
print()