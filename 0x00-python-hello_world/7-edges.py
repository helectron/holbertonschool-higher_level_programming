#!/usr/bin/python3
word = "Holberton"
word_first_3 = 'First 3 letters: {:.3}'
word_last_2 = word[7:9]
middle_word = word[1:8]
print(word_first_3.format(word))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
