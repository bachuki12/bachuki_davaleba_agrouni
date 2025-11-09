'''
დაწერეთ პროგრამა რომელიც მიიღებს ორ სტიქონს. პროგრამამ უნდა შეამოწმოს
არის თუ არა შესაძლებელი ერთი სტრიქონის სიმბოლოების გამოყენებით მეორე
სტრიქონის მიღება. შემოწმება უნდა იყოს case insensitive.
მაგალითი 1.
Input:
Listen
silent
Output: YES
მაგალითი 2.
Input:
election
collection
Output: NO
'''

# .isalpha() აის თუ არა ყველა სიმბოლო ანბანური
#.islower() შედგება თუ არა მხოლოდ პატარა ასოებისგან

input1 = input("Enter first string: ")
input2 = input("Enter second string: ")

lent_of_input1 = len(input1)
lent_of_input2 = len(input2)

def str_comparison(first_string, second_string):
    for i in first_string.lower():
        if i in second_string and lent_of_input1 >= lent_of_input2:
            return print(f"{first_string} --> {second_string}\nYes :-)")
        else:
            return print(f"{first_string} x-> {second_string}\nNo :-(")

str_comparison(input1, input2)


