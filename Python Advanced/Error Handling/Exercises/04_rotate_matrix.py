class MatrixContentError(Exception):
    pass
class MatrixSizeError(Exception):
    pass

def rotate_matrix(work_matrix):
    return list(zip(*work_matrix[::-1]))

matrix = []
while True:
    data = input()
    if not data:
        break
    try:
        data = list(map(int, data.split()))
    except ValueError:
        raise MatrixContentError('The matrix must consist of only integers')
    else:
        matrix.append(data)
if len(matrix) != len(matrix[0]):
    raise MatrixSizeError('The size of the matrix is not a perfect square')
rotated_matrix = rotate_matrix(matrix)
for row in range(len(rotated_matrix)):
    for col in range(len(rotated_matrix[row])):
        print(rotated_matrix[row][col], end=' ')
    print()