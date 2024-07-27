# delete words which start from the letter

sentence = "Python is great for people"

letter = "p"

result = []
for word in sentence.split(' '):
    if not word.lower().startswith("p"):
        result.append(word)

new_sentence = " ".join(result)
print(new_sentence)