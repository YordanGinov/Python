from collections import deque

strength_of_kick = ([int(x) for x in input().split()])
accuracy_of_kick = deque([int(x) for x in input().split()])
goals_scored = 0
STRENGTH_ACCURACY = 100

while strength_of_kick and accuracy_of_kick:
    current_strength = strength_of_kick[-1]
    current_accuracy = accuracy_of_kick[0]
    if current_strength + current_accuracy == 100:
        goals_scored += 1
        strength_of_kick.pop()
        accuracy_of_kick.popleft()
    elif current_strength + current_accuracy < 100:
        if current_strength < current_accuracy:
            strength_of_kick.pop()
        elif current_strength > current_accuracy:
            accuracy_of_kick.popleft()
        elif current_strength == current_accuracy:
            strength_of_kick[-1] += current_accuracy
            accuracy_of_kick.popleft()
    elif current_strength + current_accuracy > 100:
        strength_of_kick[-1] -= 10
        accuracy_of_kick.append(accuracy_of_kick.popleft())

if goals_scored == 3:
    print("Paul scored a hat-trick!")
elif goals_scored == 0:
    print("Paul failed to score a single goal.")
elif 0 < goals_scored < 3:
    print("Paul failed to make a hat-trick.")
else:
    print("Paul performed remarkably well!")
if goals_scored > 0:
    print(f"Goals scored: {goals_scored}")
if strength_of_kick:
    print(f"Strength values left: {', '.join([str(x) for x in strength_of_kick])}")
if accuracy_of_kick:
    print(f"Accuracy values left: {', '.join([str(x) for x in accuracy_of_kick])}")