sentence = "New, sentence, with, hope, new,sentence,with,hope"

words = set()
for word in sentence.split(","):
    words.add(word.strip())

print(words)