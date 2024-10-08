import random

words = ['apple', 'banana', 'cherry', 'date']
random_word = random.choice(words)


subWord = random.sample(random_word, 2)

print("Random word:", random_word)
print("Random characters from the word:", subWord)
