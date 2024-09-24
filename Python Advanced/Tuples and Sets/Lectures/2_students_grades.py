number_of_students = int(input())
student_data = {}

for _ in range(number_of_students):
    student_name, student_grade = tuple(input().split())
    student_grade = float(student_grade)
    if student_name not in student_data:
        student_data[student_name] = []
    student_data[student_name].append(student_grade)

for student_name, student_grades in student_data.items():
    avg_grade = sum(student_grades) / len(student_grades)
    print(f"{student_name} -> {' '.join([f'{el:.2f}' for el in student_grades])} (avg: {avg_grade:.2f})")
