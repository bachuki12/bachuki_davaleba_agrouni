''''

დაწერეთ ფუნქცია, რომელიც დაადგენს გადაცემული რიცხვი მარტივია თუ არა და დააბრუნებს True-ს მარტივის
შემთხვევაში და False-ს შედგენილის შემთხვევაში.
ფუნქციის ქვევით გამოიძახეთ ის რამდენიმე რიცხვისთვის და დაბეჭდეთ შედეგი.

'''

def simple_or_complex(num):
    c =0
    for i in range(1, num+1):
        print(num % i)
        if num % i == 0:
            c+=1
    if c == 2:
        print(f" რიცხვი {num} არის მარტივი ")
    else:
        print(f" რიცხვი {num} არის შედგენილი ")

num =  input("Enter integer: ")
num = int(num)
if int(num) and num > 0:
    simple_or_complex(num)
else:
    while(num < 0):
        num = input("Enter integer: ")
    simple_or_complex(num)
