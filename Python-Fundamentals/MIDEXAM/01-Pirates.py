# 01. Pirates

days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

add_plunder = 0
total_plunder = 0
loss = 0

for i in range(1, days+1):
    total_plunder += daily_plunder

    if i % 3 == 0:
        add_plunder = 0.5 * daily_plunder
        total_plunder += add_plunder
    if i % 5 == 0:
        # print(total_plunder)
        loss = -0.3 * total_plunder
        # print(loss)
        total_plunder += loss

    # print(total_plunder)

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = (total_plunder * 100) / expected_plunder
    print(f"Collected only {percentage:.2f}% of the plunder.")