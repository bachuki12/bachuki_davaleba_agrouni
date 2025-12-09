'''
დაწერეთ ფუნქცია, რომელიც მიიღებს ორ ნატურალურ რიცხვს 10000-მდე და ეკრანზე გამოიტანს მათ უდიდეს საერთო გამყოფს - GCD.

მაგალითი 1:
Enter a: 1000
Enter b: 400
GCD of 1000 and 400 is 200.

მაგალითი 2:
Enter a: 10000
Enter b: 17
GCD of 10000 and 17 is 1.

'''
tmp = 1

a = input("Enter number1: ")
b = input("Enter number2: ")

def gcd(a, b):
    copy_of_b = b
    copy_of_a = a
    while (b != 0):
            tmp = a % b
            a = b
            b = tmp

    print(f"GCD of {copy_of_a} and {copy_of_b} is {a}. ")

while(True):
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        if a < 10000 and b < 10000:
            gcd(a, b)
            break
        else:
            print("Input values Out of range")
            a = input("Enter correct number1: ")
            b = input("Enter correct number2: ")
    else:
        print("Input value is negative or it's not numeric :(")
        a = input("Please Enter correct number1: ")
        b = input("Please Enter correct number2: ")


