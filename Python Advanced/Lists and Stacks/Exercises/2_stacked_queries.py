number_of_queries = int(input())
my_stack = []

functions= {
    '1': lambda number: my_stack.append(int(number)),
    '2': lambda: my_stack.pop() if my_stack else None,
    '3': lambda: print(max(my_stack)) if my_stack else None,
    '4': lambda: print(min(my_stack)) if my_stack else None
}

for _ in range(number_of_queries):
    command = input().split()
    functions[command[0]](*command[1:])

print(*reversed(my_stack), sep=', ')
