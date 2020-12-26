# 01. Disneyland Journey

money_needed = float(input())
months = int(input())

saved_money = 0
spent_money = 0

for i in range(1, months+1):
    if i % 2 != 0:
        spent_money = 0.16 * saved_money
        saved_money -= spent_money

    if i % 4 == 0 and i != 1:
        bonus = 0.25 * saved_money
        saved_money += bonus

    saved_money += 0.25 * money_needed
    # print(saved_money)

if saved_money >= money_needed:
    money_souvenirs = saved_money - money_needed
    print(f"Bravo! You can go to Disneyland and you will have {money_souvenirs:.2f}lv. for souvenirs.")
else:
    money_left = money_needed - saved_money
    print(f"Sorry. You need {money_left:.2f}lv. more.")
