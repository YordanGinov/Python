row_data, column_data = [int(num) for num in input().split()]
matrix = []
# a = 97
# for row in range(row_data):
#     matrix.append([])
#     for col in range(column_data):
#         first_last_letter = chr(row + a)
#         middle_letter = chr(ord(first_last_letter) + col)
#         text = first_last_letter + middle_letter + first_last_letter
#         matrix[row].append(text)
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         print(matrix[row][col], end=" ")
#     print()

for r in range(row_data):
    for c in range(column_data):
        print(f"{chr(97 + r)}{chr(97 + c + r)}{chr(97+r)}", end=" ")
    print()