eng_pol_dict = {'house': 'dom', 'tree': 'drzewo', 'phone': 'telefon', 'city': 'miasto'}
direct_translate = input('Which language you want translate? eng / pl: ')

# veryfication of choice
if direct_translate not in ('eng', 'pl'):
    print('Bad answer! Run program once again.')
    quit()

# translation word
if direct_translate == 'eng':
    word_to_translate = input('What word do you want translate?: ')
    print(eng_pol_dict.get(word_to_translate))
elif direct_translate == 'pl':
    word_to_translate = input('What word do you want translate?: ')
    for k, v in eng_pol_dict.items():
        if v == word_to_translate:
            print(k)

