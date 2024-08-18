# reading all file

with open('test.txt', 'r') as handler:
    for line in handler:
        print(line.strip())