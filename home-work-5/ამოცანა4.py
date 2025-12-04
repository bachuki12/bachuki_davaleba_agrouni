'''
მოცემულია წინადადება:
sentence = "Data Science is fun and Data Analysis is powerful if data is understood well."
1) შექმენით სია რომლის წევრებიც იქნება წინადადების სიტყვები.
2) map + lambda-ს გამოყენებით გადაწერეთ ზევით შექმნილი სიის წევრები პატარა ასოებით.
3) functools.reduce +lambda-ს გამოყენებით შექმენით ლექსიკონი {word: count}
რომლის გასაღებებიც იქნება სიტყვები და მნიშვნელობები იქნება მათი რაოდენობა წინადადებაში.
4) max(…, key = ...)-ს გამოყენებით იპოვეთ ყველაზე ხშირად გამეორებული სიტყვა.
5) filter + lambda-ს გამოყენებით დატოვეთ სიტყვები რომლებიც შეიცავს 3-ზე მეტ ასოს.

'''

from functools import reduce

sentence = "Data Science is fun and Data Analysis is powerful if data is understood well."

split_sentence = sentence.split()
'''
2) map + lambda-ს გამოყენებით გადაწერეთ ზევით შექმნილი სიის წევრები პატარა ასოებით.
'''

list_of_little_words = list(map(lambda x: x.lower(), split_sentence))
print(list_of_little_words)

# p = ['data', 'science', 'is', 'fun', 'and', 'data', 'analysis', 'is', 'powerful', 'if', 'data', 'is', 'understood', 'well.']

'''
3) functools.reduce +lambda-ს გამოყენებით შექმენით ლექსიკონი {word: count} 
რომლის გასაღებებიც იქნება სიტყვები და მნიშვნელობები იქნება მათი რაოდენობა წინადადებაში.
'''
my_dict = {}
for word in list_of_little_words:
    my_dict.update(reduce(lambda x, y: ({word: list_of_little_words.count(word)}),list_of_little_words))

print(my_dict)

'''
4) max(…, key = ...)-ს გამოყენებით იპოვეთ ყველაზე ხშირად გამეორებული სიტყვა.
'''
most_common_word = max(my_dict, key=lambda k: my_dict[k])
print(f"{most_common_word.capitalize()} --> appears {my_dict[most_common_word]} times")

'''
5) filter + lambda-ს გამოყენებით დატოვეთ სიტყვები რომლებიც შეიცავს 3-ზე მეტ ასოს.
'''

more_than_3_symbols = list(filter(lambda x: len(x)>3, my_dict))
print(more_than_3_symbols)
