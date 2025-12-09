
'''დაწერეთ ფუნქცია, რომელიც მიიღებს ორ ნატურალურ რიცხვს
10000-მდე და ეკრანზე გამოიტანს მათ უმცირეს საერთო ჯერადს - LCM.
იმპორტი გაუკეთეთ საერთო გამყოფის ფუნქციას წინა მაგალითიდან და მისი საშუალებით
დაათვლევინეთ უმცირესი საერთო ჯერადი.
მინიშნება: lcm(a, b) = a * b / gcd(a, b).
მაგალითი 1:
Enter a: 1000
Enter b: 400
LCM of 1000 and 400 is 2000.
მაგალითი 2:
Enter a: 500
Enter b: 50
LCM of 500 and 50 is 500.
ფუნქციის ქვევით გამოიძახეთ ის რამდენიმეჯერ და დარწმუნდით მის სისწორეში.
'''
from GCD import gcd

tmp = 1

a = input("Enter number1: ")
b = input("Enter number2: ")
copy_of_b = b
copy_of_a = a
while(True):
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        if a < 10000 and b < 10000:
            break
        else:
            print("Input values Out of range")
            a = input("Enter correct number1: ")
            b = input("Enter correct number2: ")
    else:
        print("Input value is negative or it's not numeric :(")
        a = input("Please Enter correct number1: ")
        b = input("Please Enter correct number2: ")

def lcm(a, b):
    val_lcm = int(a * b / gcd(a, b))
    return  f"LCM of {copy_of_a} and {copy_of_b} is {val_lcm}."

print(lcm(a, b))

