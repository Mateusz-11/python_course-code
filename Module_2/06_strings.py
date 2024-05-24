# task1
sentence = "Pies to najlepszy przyjaciel człowieka, lecz nie każy pies o tym wie."
print(sentence.lower().count("pies"))

# Task2
pass_to_change = 'Aadminus'

new_pass = pass_to_change.lower().replace('a', "@")
new_pass = new_pass.lower().replace('s', "$")

print(pass_to_change)
print(new_pass)

#task 3
sentence_2 = "12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek"

list_of_words = sentence_2.split(' ')
print(list_of_words)

total = 0
for i in list_of_words:
    if i.isnumeric():
        total += int(i)
print(f'Sum is equal: {total}')
