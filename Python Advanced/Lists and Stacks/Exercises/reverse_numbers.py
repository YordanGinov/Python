program_input = input().split()
stack = []
for number in program_input:
    stack.append(number)
print(" ".join(reversed(stack)))
