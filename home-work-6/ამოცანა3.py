'''

დაწერეთ პროგრამა რომელიც წინა ამოცანაში აღწერილი სტრუქტურის ფაილიდან
წაიკითხავს გაყიდვების ინფორმაციას.
a. პროგრამამ უნდა იპოვოს მაქსიმალური შესყიდვის (პროდუქტების რაოდენობით, ერთ
შესყიდვაში) განმხორციელებელი მომხმარებელი, თუ რამდენიმენა, მაშინ
მომხმარებლების სია.
b. პროგრამამ უნდა იპოვოს მაქსმალური შესყიდვის (ყველა შესყიდვის ჯამური
ღირებულებით) განმხორციელებელი მომხმარებელი, თუ რამდენიმენა, მაშინ
მომხმარებლების სია.
c. პროგრამამ უნდა იპოვოს შესყიდვების ღირებულების საშუალო არითმეტიკული.
d. პროგრამამ უნდა იპოვოს შესყიდვების რაოდენობების საშუალო არითმეტიკული.
e. პროგრამამ უნდა იპოვოს ყველაზე დიდი რაოდენობით გაყიდული პროდუქტი, თუ
რამდენიმეა მაშინ, პროდუქტების სია.
ნაპოვნი მონაცემები შეაგროვეთ dict ტიპის ობიექტში და ჩაწერეთ stats.json ფაილში.
დააფორმატეთ stats.json ფაილი ისე, რომ მონაცემები ჩაიწეროს ადვილად წაკითხვადი
ფორმით.

'''
import json
from collections import defaultdict

# -------------------------------
# 1. ფაილიდან მონაცემების წაკითხვა
# -------------------------------
with open("data.txt", "r") as f:
    data = [line.strip().split(",") for line in f]

# ---------------------------------
# 2. დამხმარე ცვლადების ინიციალიზაცია
# ---------------------------------
max_single_purchase = 0
users_max_single_purchase = set()

user_total_value = defaultdict(float)

total_value = 0
total_amount = 0
purchase_count = 0

product_total_amount = defaultdict(int)

# -------------------------------
# 3. მონაცემების დამუშავება
# -------------------------------
for name, product, amount, price in data:
    amount = int(amount)
    price = float(price)

    purchase_value = amount * price

    # a) მაქსიმალური ერთჯერადი შესყიდვა (რაოდენობით)
    if amount > max_single_purchase:
        max_single_purchase = amount
        users_max_single_purchase = {name}
    elif amount == max_single_purchase:
        users_max_single_purchase.add(name)

    # b) მომხმარებლის ჯამური შესყიდვის ღირებულება
    user_total_value[name] += purchase_value

    # c და d) საერთო ჯამები საშუალოსთვის
    total_value += purchase_value
    total_amount += amount
    purchase_count += 1

    # e) პროდუქტის გაყიდული რაოდენობა
    product_total_amount[product] += amount

# ---------------------------------------
# 4. მაქსიმალური ჯამური ღირებულების მქონე მომხმარებელი
# ---------------------------------------
max_total_value = max(user_total_value.values())
users_max_total_value = [
    name for name, value in user_total_value.items()
    if value == max_total_value
]

# -------------------------------
# 5. საშუალო არითმეტიკულები
# -------------------------------
average_purchase_value = total_value / purchase_count
average_purchase_amount = total_amount / purchase_count

# -------------------------------
# 6. ყველაზე მეტი რაოდენობით გაყიდული პროდუქტი
# -------------------------------
max_product_amount = max(product_total_amount.values())
top_products = [
    product for product, amount in product_total_amount.items()
    if amount == max_product_amount
]

# -------------------------------
# 7. შედეგების შეგროვება dict-ში
# -------------------------------
stats = {
    "max_single_purchase_amount": {
        "amount": max_single_purchase,
        "users": sorted(users_max_single_purchase)
    },
    "max_total_purchase_value": {
        "value": max_total_value,
        "users": sorted(users_max_total_value)
    },
    "average_purchase_value": average_purchase_value,
    "average_purchase_amount": average_purchase_amount,
    "top_selling_products": {
        "amount": max_product_amount,
        "products": sorted(top_products)
    }
}

# -------------------------------
# 8. ჩაწერა stats.json ფაილში
# -------------------------------
with open("stats.json", "w", encoding="utf-8") as f:
    json.dump(stats, f, indent=4, ensure_ascii=False)

print("სტატისტიკა წარმატებით ჩაიწერა stats.json ფაილში")




