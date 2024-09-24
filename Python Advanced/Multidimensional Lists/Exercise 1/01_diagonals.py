matrix = [[int(num) for num in input().split(', ')] for row in range(int(input()))]
primary_diagonal = []
secondary_diagonal = []

for i, j in zip(range(0, len(matrix)), range(len(matrix) -1, -1, -1)):
    a = matrix[i][i]
    b = matrix[i][j]
    primary_diagonal.append(a)
    secondary_diagonal.append(b)

print(f'Primary diagonal: {", ".join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')