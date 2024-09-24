rows,columns = [int(el) for el in input().split()]
matrix = [[] for row in range(rows)]
bunny_position = []
new_bunny_positions = []
has_won = False
has_lost = False
for row in range(rows):
    row_data = input()
    for element in range(len(row_data)):
        if row_data[element] == "P":
            player_row_position = row
            player_col_position = element
        elif row_data[element] == "B":
            bunny_position.append([row,element])
        matrix[row].append(row_data[element])
commands = input()
for command in commands:
    if command == "U":
        if player_row_position - 1 < 0:
            has_won = True
            matrix[player_row_position][player_col_position] = "."
        else:
            if [player_row_position-1,player_col_position] in bunny_position:
                has_lost = True
            else:
                matrix[player_row_position - 1][player_col_position] = "P"
            matrix[player_row_position][player_col_position] = "."
            player_row_position -= 1
    elif command == "D":
        if player_row_position + 1 >= rows:
            has_won = True
            matrix[player_row_position][player_col_position] = "."
        else:
            if [player_row_position+1,player_col_position] in bunny_position:
                has_lost = True
            else:
                matrix[player_row_position + 1][player_col_position] = "P"
            matrix[player_row_position][player_col_position] = "."
            player_row_position += 1
    elif command == "L":
        if player_col_position - 1 < 0:
            has_won = True
            matrix[player_row_position][player_col_position] = "."
        else:
            if [player_row_position,player_col_position-1] in bunny_position:
                has_lost = True
            else:
                matrix[player_row_position][player_col_position - 1] = "P"
            matrix[player_row_position][player_col_position] = "."
            player_col_position -= 1
    elif command == "R":
        if player_col_position + 1 >= columns:
            has_won = True
            matrix[player_row_position][player_col_position] = "."
        else:
            if [player_row_position,player_col_position+1] in bunny_position:
                has_lost = True
            else:
                matrix[player_row_position][player_col_position + 1] = "P"
            matrix[player_row_position][player_col_position] = "."
            player_col_position += 1
    new_bunny_positions.clear()
    for bunny in bunny_position:
        if bunny[0] - 1 >= 0:
            bunny_up= [bunny[0]-1, bunny[1]]
            matrix[bunny[0] -1][bunny[1]] = "B"
            new_bunny_positions.append(bunny_up)
        if bunny[0] + 1 < rows:
            bunny_down= [bunny[0]+1, bunny[1]]
            matrix[bunny[0] + 1][bunny[1]] = "B"
            new_bunny_positions.append(bunny_down)
        if bunny[1] - 1 >= 0:
            bunny_left= [bunny[0], bunny[1]-1]
            matrix[bunny[0]][bunny[1] - 1] = "B"
            new_bunny_positions.append(bunny_left)
        if bunny[1] + 1 < columns:
            bunny_right= [bunny[0], bunny[1]+1]
            matrix[bunny[0]][bunny[1] + 1] = "B"
            new_bunny_positions.append(bunny_right)
    for new_bunny in new_bunny_positions:
        if new_bunny not in bunny_position:
            bunny_position.append(new_bunny)
    if [player_row_position,player_col_position] in bunny_position and has_won == False:
        has_lost = True
    if has_won:
        for row in range(rows):
            for col in range(columns):
                print(matrix[row][col], end='')
            print()
        print(f"won: {player_row_position} {player_col_position}")
        exit()
    if has_lost:
        for row in range(rows):
            for col in range(columns):
                print(matrix[row][col], end='')
            print()
        print(f'dead: {player_row_position} {player_col_position}')
        exit()
