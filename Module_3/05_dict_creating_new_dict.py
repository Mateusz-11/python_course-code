text = 'raz raz dwa trzy trzy trzy raz'

list_words = text.split()
print(list_words)

counter_words = {}

for word in list_words:
    if word not in counter_words.keys():
        counter_words[word] = 1
    else:
        print('update value')
        counter_words.update({word: counter_words[word] + 1})

print(counter_words)
