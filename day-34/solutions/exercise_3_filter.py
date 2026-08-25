words = ["apple", "banana", "orange", "kiwi", "elderberry"]

vowels = "aeiou"
vowel_words = list(filter(lambda word: word[0] in vowels, words))
print(vowel_words)
