clothes = (input().split())
rack_capacity = int(input())
current_capacity = rack_capacity
racks = 0

while clothes and rack_capacity > 0:
    racks += 1
    while clothes and current_capacity > 0:
        current_clothes = int(clothes.pop())
        if current_capacity > current_clothes:
            current_capacity -= current_clothes
        elif current_capacity == current_clothes:
            current_capacity = rack_capacity
            break
        else:
            clothes.append(str(current_clothes))
            current_capacity = rack_capacity
            break
print(racks)
