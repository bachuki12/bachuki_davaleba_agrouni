'''

დაწერეთ პროგრამა რომელიც წაიკითხავს data.txt ფაილს. ამ ფაილში მოცემულია
პროდუქციის შესყიდვის მონაცემები. მონაცემები ერთმანეთისგან გამოყოფილია მძიმით.
მონაცემების მიმდევრობა შემდეგია user_name,product_name,amount,price - სადაც price
არის ერთეული პროდუქციის ღირებულება. პროგრამამ უნდა გააკეთოს ორი ახალი
ფაილი small.txt და high.txt. პროგრამა small.txt ფაილში უნდა გადაწეროს ის შესყიდვები
რომელთა ღირებულება ნაკლებია 10-ზე, ხოლო ყველა სხვა დანარჩენი high.txt ფაილში.

'''

with open('data.txt','r') as data:
    values = data.read().splitlines()

user_names_list = [values[i].split(',')[0] for i in range(len(values))]
product_name_list = [values[i].split(',')[1] for i in range(len(values))]
amount = [int(values[i].split(',')[2]) for i in range(len(values))]
price = [float(values[i].split(',')[3]) for i in range(len(values))]
all_price = []

for i in range(len(user_names_list)):
    all_price.append({"name":user_names_list[i], "product_name":product_name_list[i], "amount":amount[i], "price":price[i]})

smal = list(filter(lambda x: x["amount"]*x["price"]<10, all_price))
high = list(filter(lambda x: x["amount"]*x["price"]>10, all_price))

new_list_small = ""
new_list_high = ""

for i in range(len(smal)):
    new_list_small+=(smal[i]["name"]+" "+ smal[i]["product_name"]+" "+str(smal[i]["amount"])+" "+str(smal[i]["price"])+"\n")

for i in range(len(high)):
    new_list_high+=(high[i]["name"]+ " "+ high[i]["product_name"]+" "+str(high[i]["amount"])+" "+str(high[i]["price"])+"\n")

with open('small.txt','w') as add_products:
        add_products.writelines(new_list_small)

with open('high.txt','w') as high_add_products:
    high_add_products.writelines(new_list_high)

