# Create loop which output contains words with the same first and the last letter.

sentence = "Litwo ojczyzno moja Ty jesteś jak zdrowie"

for word in sentence.split():
    if word[0].lower() == word[-1].lower():
        print(word)

# result: ojczyzno
