def word_count(input_text):
    word_list = input_text.lower().split()
    word_stats = {}
    for word in word_list:
        word = word.strip(".,!?\"'():;")
        word_stats[word] = word_stats.get(word, 0) + 1
    return word_stats

input_text = input("Введіть текст: ").strip().lower()
word_stats = word_count(input_text)
frequent_items = [word for word, count in word_stats.items() if count > 3]

print("Даний текст:", input_text)
print("Словник тексту:", word_stats)
print("Слова, що зустрічаються більше 3 разів:", frequent_items)

"""Це абсолютно точно не текст, що абсолютно точно не використовується в тесті для не абсолютно точно не точної прорами."""