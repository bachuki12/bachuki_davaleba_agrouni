from functools import reduce

#1) წინადადება და სიტყვების სია
sentence = "Data Science is fun and Data Analysis is powerful if data is understood well."
words = sentence.split()  # სიტყვების სია
print("Step 1:", words)

# 2) map + lambda -> ყველა სიტყვას ჩავწერთ პატარა ასოებში
lower_words = list(map(lambda w: w.lower(), words))
print("Step 2:", lower_words)

# 3) reduce + lambda -> სიტყვების რაოდენობის ლექსიკონი
word_counts = reduce(
    lambda acc, w: {**acc, w: acc.get(w, 0) + 1},
    lower_words,
    {}
)
print("Step 3:", word_counts)

#4) max(..., key=...) -> ყველაზე ხშირად განმეორებული სიტყვა
most_common_word = max(word_counts, key=lambda k: word_counts[k])
print("Step 4:", most_common_word, "appears", word_counts[most_common_word], "times")

# 5) filter + lambda -> დატოვეთ სიტყვები რომლებიც შეიცავს 3-ზე მეტ ასოს
long_words = list(filter(lambda w: len(w) > 3, lower_words))
print("Step 5:", long_words)
