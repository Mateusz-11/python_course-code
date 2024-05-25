text = '123. Be or not to be!'

new_text = ""
for i in text:
    if i.isalpha() or i.isdigit():
        new_text += i

print(new_text)
