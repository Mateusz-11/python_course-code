word1 = "asdfghjklaccab"
word2 = "fgahjskldaccab"

list1 = list(word1)
list2 = list(word2)

# print(sorted(list1))
# print(sorted(list2))

if sorted(list1) == sorted(list2):
    print("These words are anagrams")
else:
    print("These words aren't anagrams")