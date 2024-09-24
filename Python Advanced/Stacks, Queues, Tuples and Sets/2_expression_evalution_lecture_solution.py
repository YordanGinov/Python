from collections import deque
from math import floor

user_input = input().split()
queue = deque()


def calculate(a:int, b:int, operator:str)->int:
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a // b

for c in user_input:
    if c not in '+-*/':
        queue.append(int(c))
    else:
        while len(queue) > 1:
            num_1 = queue.popleft()
            num_2 = queue.popleft()
            queue.append(calculate(num_1, num_2, c))
print(queue.popleft())