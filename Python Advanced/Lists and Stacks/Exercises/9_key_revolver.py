from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets_in_barrel = gun_barrel_size
number_of_bullets = deque(input().split())
locks = deque(input().split())
intelligence_value = int(input())
money_earned = intelligence_value

while number_of_bullets and locks:
    if bullets_in_barrel <= 0:
        print('Reloading!')
        bullets_in_barrel = gun_barrel_size
    else:
        current_bullet = int(number_of_bullets.pop())
        current_lock = int(locks.popleft())
        money_earned -= bullet_price
        bullets_in_barrel -= 1
        if current_bullet <= current_lock:
            print("Bang!")
        else:
            print("Ping!")
            locks.appendleft(str(current_lock))
if bullets_in_barrel <= 0 and number_of_bullets:
    print('Reloading!')
if len(locks) <= 0:
    print(f'{len(number_of_bullets)} bullets left. Earned ${money_earned}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
