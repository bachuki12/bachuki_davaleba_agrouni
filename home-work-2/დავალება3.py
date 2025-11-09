'''
დაწერეთ პროგრამა რომელიც დააგენერირებს 5 ცალ შემთხვევით რიცხვს 1-დან 4-მდე
და ჩაწერს სიაში. პროგრამამ უნდა გადაუაროს სიას და თითოეული ელემენტისთვის ეს
ელემენტი ჩაწეროს ახალ სიაში, იმდენჯერ, რაც არის მისი მნიშვნელობა. დაბეჭდეთ
ახალი სიის სიგრძე და თვითონ სია ეკრანზე.
მაგალითი: ვთქვათ პროგრამამ დააგენერირა სია, [1, 4, 2, 2, 3].
უნდა დაიბეჭდოს
List - [1, 4, 4, 4, 4, 2, 2, 2, 2, 3, 3, 3]
Length - 12
'''
from operator import length_hint

'''
random_num_list = [random.randint(1, 4) for i in range(5)]
print(random_num_list)
'''


import  random

random_num_list = []
final_random_num_list = []
count_list = []
n = 5

for i in range(n):
    random_num_list.append(random.randint(0, 4))
    for k in range(random_num_list[i]):
        final_random_num_list.append(random_num_list[i])


final_random_num_list_length = len(final_random_num_list)
final_random_num_list.sort()

print(f"list =  {final_random_num_list}")
print(f"lenght  - {final_random_num_list_length}")
