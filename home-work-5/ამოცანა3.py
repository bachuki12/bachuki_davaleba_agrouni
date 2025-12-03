'''
მოცემულია მაღაზიაში არსებული პროდუქტების სახელი, ფასი და რაოდენობა:
products = [
    ("Keyboard", 49.99, 3),
    ("Mouse", 19.99, 0),
    ("Monitor", 159.99, 2),
    ("USB Cable", 4.99, 10),
    ("Headphones", 89.99, 1)
]
1) filter + lambda-ს გამოყენებით მოაცილეთ
პროდუქტი რომელიც მარაგში არ არის.

2) map + lambda-ს გამოყენებით გამოთვალეთ
თითოეული პროდუქტის ჯამური ფასი (ერთის ფასი * რაოდენობა).

3) functools.reduce + lambda-ს გამოყენებით გამოთვალეთ
მაღაზიაში არსებული ყველა ხელმისაწვდომი პროდუქტის ჯამური ფასი.
'''

products = [
    ("Keyboard", 49.99, 3),
    ("Mouse", 19.99, 0),
    ("Monitor", 159.99, 2),
    ("USB Cable", 4.99, 10),
    ("Headphones", 89.99, 1)
]

product_dict = []
for i in products:
    product_dict.append({"Pname":i[0], "Pprice":i[1], "Pquantity":i[2]})

# for i in product_dict:
#     print(i)
'''
1) filter + lambda-ს გამოყენებით მოაცილეთ პროდუქტი რომელიც მარაგში არ არის.
'''
products_in_stock = list(filter(lambda x: x['Pquantity'] >0, product_dict))

for i in products_in_stock :
    print(i)

'''

2) map + lambda-ს გამოყენებით გამოთვალეთ
თითოეული პროდუქტის ჯამური ფასი (ერთის ფასი * რაოდენობა).

'''
grund_sum = list(map(lambda x: x['Pprice']*x["Pquantity"], products_in_stock))
k = 0

for i in products_in_stock:
    print(f"{i["Pname"]} Grund_sum = {grund_sum[k]}")
    k+=1
'''
3) functools.reduce + lambda-ს გამოყენებით გამოთვალეთ
მაღაზიაში არსებული ყველა ხელმისაწვდომი პროდუქტის ჯამური ფასი.
'''
from functools import reduce
all_product_price = reduce(lambda x, y: x+y, grund_sum)

print(f"მაღაზიაში არსებული ყველა ხელმისაწვდომი პროდუქტის ჯამური ფასია {all_product_price}$")