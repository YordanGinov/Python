from collections import deque
from math import floor

expression = deque([el for el in input().split()])
numbers = deque()
current_sum = 0

for element in expression:
    if element not in '+-*/':
        numbers.append(int(element))
    elif element == '+':
        current_sum = numbers.popleft()
        while numbers:
            current_sum += numbers.popleft()
        numbers.appendleft(current_sum)
    elif element == '-':
        current_sum = numbers.popleft()
        while numbers:
            current_sum -= numbers.popleft()
        numbers.appendleft(current_sum)
    elif element == '*':
        current_sum = numbers.popleft()
        while numbers:
            current_sum *= numbers.popleft()
        numbers.appendleft(current_sum)
    elif element == '/':
        current_sum = numbers.popleft()
        while numbers:
            current_sum = floor(current_sum / numbers.popleft())
        numbers.appendleft(current_sum)
print(numbers.popleft())
