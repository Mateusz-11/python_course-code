def repeat_text(text, delimiter=",", repeat=1):
    output = []
    for _ in range(repeat):
        output.append(text)
    return delimiter.join(output)

print(repeat_text("Ala ma kota"))
print(repeat_text("Python", delimiter=";",repeat=3))

