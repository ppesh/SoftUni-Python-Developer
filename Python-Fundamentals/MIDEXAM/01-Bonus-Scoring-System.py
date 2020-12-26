# 01. Bonus Scoring Sysem

# Solution I:
"""
import math
students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

max_bonus = 0
max_bonus_attendances = 0

if lectures_count > 0 and students_count > 0:
    for student in range(students_count):
        attendances = int(input())
        total_bonus = attendances / lectures_count * (5 + additional_bonus)
        if total_bonus >= max_bonus:
            max_bonus = total_bonus
            max_bonus_attendances = attendances

print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {max_bonus_attendances} lectures.')
"""

# Solution II:
"""
import math
students = int(input())
lectures = int(input())
initial_bonus = int(input())
attendance_list = []

if lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    for i in range(1, students + 1):
        attendances = int(input())
        attendance_list.append(attendances)
    
    print(f'Max Bonus: {math.ceil((max(attendance_list) / lectures) * (5 + initial_bonus))}.')
    print(f'The student has attended {max(attendance_list)} lectures.')
"""