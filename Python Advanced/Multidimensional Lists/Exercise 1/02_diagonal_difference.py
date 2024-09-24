matrix = [[int(num) for num in input().split()] for row in range(int(input()))]
primary_diagonal = []
secondary_diagonal = []

for i, j in zip(range(0, len(matrix)), range(len(matrix) -1, -1, -1)):
    a = matrix[i][i]
    b = matrix[i][j]
    primary_diagonal.append(a)
    secondary_diagonal.append(b)

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
