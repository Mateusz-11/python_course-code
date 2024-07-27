text_source = "Text to encrypt"
text = text_source.upper()
shift = 1
print(f"Text to encrypt: {text}")

encrypted_text= ""
for character in text:
    if character.isalpha():
        character = (chr(ord(character) + shift))
    encrypted_text += character

decrypted_text= ""
for character in encrypted_text:
    if character.isalpha():
        character = (chr(ord(character) - shift))
    decrypted_text += character

print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")






