'''
დაწერეთ ფუნქცია რომელიც არგუმენტად მიიღებს ნატურალურ რიცხვს n.
ფუნქციამ უნდა დააგენერიროს n ცალი შემთხვევითი რიცხვების a, b წყვილი,
სადაც 0<a<1 და 0<b<1. ფუნქციაში შემოიღეთ მთვლელი counter = 0,
თუ დაგენერირებული რიცხვები აკმაყოფილებს პირობას math.sqrt(a ** 2 + b ** 2) <= 1,
counter-ის მნიშვნელობა გაზარდეთ 1-ით. ფუნქციას დააბეჭდინეთ 4 * counter / n.
გამოიძახეთ ფუნქცია რამდენჯერმე და გადაეცით არგუმენტებად 10, 1000, 100000, 10000000.
რას ამჩნევთ? ახსენით მიღებული შედეგი.
'''
import random
import math

# integer = input("Enter integer:-> ")
#
# while True:
#     if integer.isdigit():
#         integer = int(integer)
#         break
#     else:
#         integer = input("Enter correct integer:-> ")

counter = 0
def my_func(integer):
    global counter
    for i in range(integer):
        a = random.uniform(0, 1)
        b = random.uniform(0, 1)
        if math.sqrt(a ** 2 + b ** 2) <= 1:
            counter +=1
            print(f"4 * counter / integer = {4 * counter / integer}")
'''
როგორც დავაკვირდი ბოლო დაგენერეირებული რიცხვების ბოლო მნიშვნელობები მეორდება (4, 8, 2, 6)_ით
მაგალითად პირველი არის 0.4, 0.8, 0.12, 0.16
შემდეგ ბოლო ციფრები არ იცვლება მხოლოდ წინები 1.4, 1.8, 1.12, 1.16
შემდეგ 2.4 2.8 2.12 2.16

'''

my_func(10)
my_func(100)
my_func(1000)
my_func(10000)

