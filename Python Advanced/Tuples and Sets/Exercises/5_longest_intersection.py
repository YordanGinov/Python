def work_on_input(work_data):
    work_set = set()
    first_part, second_part = work_data.split(',')
    for num in range(int(first_part), int(second_part)+1):
        work_set.add(num)
    return work_set

n = int(input())
first_set = set()
second_set = set()
multi_numbers = set()
highest_multi_set= set()
highest_multi_set_len = 0

for _ in range(n):
    first, second = input().split('-')
    first_set = work_on_input(first)
    second_set = work_on_input(second)
    multi_numbers = first_set.intersection(second_set)
    if len(multi_numbers) > highest_multi_set_len:
        highest_multi_set_len = len(multi_numbers)
        highest_multi_set = multi_numbers
print(f"Longest intersection is {''.join(str([el for el in highest_multi_set]))} with length {highest_multi_set_len}")
