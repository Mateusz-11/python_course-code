correct_lines = []
with open('h_05_mess.txt', encoding='utf8') as file:
    for line in file:
        if "Java Script" not in line:
            line = line.replace('Java', 'Python')

        correct_lines.append(line.strip())

with open('h_05_mess_new.txt', "w", encoding='utf8') as file:
    file.write('\n'.join(correct_lines))


