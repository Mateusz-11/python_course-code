sentance = "Be or not To be"

print(sentance)
result = ""

# I version
# for counter, word in enumerate(sentance.split(' ')):
#     if counter % 2 == 0:
#         result += word.upper()
#     else:
#         result += word.lower()
#
# print(result)

# II version
new_sentance = ""
for counter, word in enumerate(sentance.split(' ')):
    new_word = word.upper()
    if counter % 2 != 0:
        new_word = word.lower()

    new_sentance = f'{new_sentance}{new_word} '

print(new_sentance)
