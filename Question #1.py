# Question 1

import string
with open ("sample-file.txt", "r") as file:
    data = file.read()

tokens = data.split()
word_count = {}

for word in tokens:
    word = word.lower()
    word = word.strip(string.punctuation)

    if sum(char.isalpha() for char in word) >= 2:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words[:10]:
    print(f"{word} -> {count}")