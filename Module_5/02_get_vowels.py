def get_vowels(word):
    letters = []
    for character in word:
        character = character.lower()
        if character in ('a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y') and character not in letters:
            letters.append(character)
    return letters

print(get_vowels("test"))
print(get_vowels("LorEm"))