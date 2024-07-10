text = input("Enter a sentence: ")
word = []

def words(text):
    words = ''
    for char in text:
        if char.isspace():
            if words:
                word.append(words)
                words = ''
        else:
            words += char
    if words:
        word.append(words)

words(text)
print(word)
