text = 'raz raz dwa trzy trzy trzy raz'

list_words = text.split()
print(list_words)
counter_words = {}

# 1 version
# for word in list_words:
#     if word not in counter_words.keys():
#         counter_words[word] = 1
#     else:
#         counter_words.update({word: counter_words[word] + 1})

## 2 version
for word in list_words:
    counter_words[word] = counter_words.get(word, 0) + 1

print(counter_words)
