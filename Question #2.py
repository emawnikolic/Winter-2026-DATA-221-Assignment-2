# Question 2

import string
with open("sample-file.txt", "r") as file:
    text = file.read()

tokens = text.split()
cleaned_tokens = []

for token in tokens:
    token = token.lower()
    token = token.strip(string.punctuation)

    if sum(char.isalpha() for char in token) >= 2:
        cleaned_tokens.append(token)

bigrams = []

for i in range(len(cleaned_tokens)-1):
    bigram = (cleaned_tokens[i], cleaned_tokens[i+1])
    bigrams.append(bigram)

bigram_counts = {}

for bigram in bigrams:
    if bigram in bigram_counts:
        bigram_counts[bigram] += 1
    else:
        bigram_counts[bigram] = 1

sorted_bigrams = sorted(bigram_counts.items(), key=lambda x: x[1], reverse=True)

for (word1, word2), count in sorted_bigrams[:5]:
    print(f"{word1} {word2} -> {count}")