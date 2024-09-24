#Input
from collections import deque
bees = deque([int(el) for el in input().split()])
nectar = [int(el) for el in input().split()]
symbols = deque(input().split())
honey_made = 0

#Functions
def calculations(a: int, b: int, symbol: str):
    if operator == "+":
        return abs(a + b)
    elif operator == "-":
        return abs(a - b)
    elif operator == "*":
        return abs(a * b)
    elif operator == "/":
        if n == 0:
            return 0
        else:
            return abs(a / b)


#Logic
while bees and nectar and symbols:
    if bees[0] <= nectar[-1]:
        operator = symbols.popleft()
        bee = bees.popleft()
        n = nectar.pop()
        honey_made += calculations(bee, n, operator)
    else:
        nectar.pop()
#Output
print(f'Total honey made: {honey_made}')
if bees:
    print(f'Bees left: {", ".join([str(el) for el in bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(el) for el in nectar])}')
