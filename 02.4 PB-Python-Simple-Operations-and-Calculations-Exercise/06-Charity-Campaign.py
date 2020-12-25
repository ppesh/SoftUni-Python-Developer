# 06.Charity Campaign

days = int(input())
confectioners = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

cake_price = 45
waffle_price = 5.80
pancake_price = 3.20

money_day = confectioners * ((cakes * cake_price) + (waffles * waffle_price) + (pancakes * pancake_price))
money_total = days * money_day
money = money_total - (money_total/8)

print(f'{money:.2f}')






