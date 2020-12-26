# 01. National Court

employee_1_eff = int(input())
employee_2_eff = int(input())
employee_3_eff = int(input())
people_count = int(input())

people_per_hour = employee_1_eff + employee_2_eff + employee_3_eff
time_needed = 0

while people_count > 0:
    time_needed += 1
    if time_needed % 4 == 0:
        continue
    people_count -= people_per_hour

print(f"Time needed: {time_needed}h.")
