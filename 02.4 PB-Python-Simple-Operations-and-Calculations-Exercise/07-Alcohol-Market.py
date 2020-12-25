# 07.Alcohol Market

whiskey_price = float(input())      # per liter
beer_L = float(input())
wine_L = float(input())
raki_L = float(input())
whiskey_L = float(input())

raki_price = whiskey_price/2
wine_price = raki_price - (0.40 * raki_price)
beer_price = raki_price - (0.80 * raki_price)

whiskey = whiskey_L * whiskey_price
beer = beer_L * beer_price
wine = wine_L * wine_price
raki = raki_L * raki_price

money = whiskey + beer + wine +raki

print(f'{money:.2f}')





