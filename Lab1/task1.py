def word_count(text):
    words = text.lower().split()
    word_dict = {}
    for word in words:
        word = word.strip(".,!?\"'():;")
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

text = input("Введіть текст: ").strip().lower()
"""Це абсолютно точно не текст, що абсолютно точно не використовується в тесті для не абсолютно точно не точної прорами."""

counts = word_count(text)
frequent_words = [word for word, count in counts.items() if count > 3]

print("Даний текст:", text)
print("Словник тексту:", counts)
print("Слова, що зустрічаються більше 3 разів:", frequent_words)

