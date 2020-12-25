# 04.Tailoring Shop

tables = int(input())
length = float(input())     # in m
width = float(input())      # in m

p = 7   # $, rectangular
k = 9   # $, square

p_area = tables * (length + 2 * 0.30) * (width + 2 * 0.30)
# print(p_area)

k_area = tables * (length/2) * (length/2)
# print(k_area)

e_rate = 1.85   # lv

price_USD = (p_area * p) + (k_area * k)
price_BGN = price_USD * 1.85

print(f'{price_USD:.2f} USD')
print(f'{price_BGN:.2f} BGN')


