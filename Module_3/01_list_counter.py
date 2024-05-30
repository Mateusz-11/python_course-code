sentence = input('Write sentence: ')
list_from_sentence = sentence.split(' ')

print(f'Number of words: {len(list_from_sentence)}')
amount_of_characters = 0

# counter of characters in elements of list
for i in list_from_sentence:
    for j in i:
        amount_of_characters += 1

print(f'Number of characters: {amount_of_characters}')

