rows, columns = [int(el) for el in input().split(", ")]
matrix = []
elements_sum=0
for i in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)
    elements_sum += sum(elements)

print(elements_sum)
print(matrix)
