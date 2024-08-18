# 1 version
handler = open('test.txt')
line = handler.readline()
print(line)
handler.close()

# 2 version
with open('text.txt') as handler:
    line = handler.readline()
    print(line)