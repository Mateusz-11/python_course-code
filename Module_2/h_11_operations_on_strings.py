sentence = "Litwo ojczyzno moja Ty jesteś jak zdrowie"

for word in sentence.split():
    if word[0].lower() == word[-1].lower():
        print(word)

