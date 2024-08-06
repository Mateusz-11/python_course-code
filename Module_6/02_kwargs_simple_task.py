def count_words(*args, ignore_case=True):
    output = {}

    for arg in args:
        arg = arg.lower() if ignore_case else arg
        output[arg] = output.get(arg, 0) + 1

    for k, v in output.items():
        if v == max(output.values()):
            return k, v



print(count_words("Python", "python", "Python", "java", "Java","Python", "Python", "Python", "java", "JavaScript", "Javascript", "Go", "Go", ignore_case=True))
print('- - - ' * 5)
print(count_words("Python", "python", "Python", "java", "Java","Python", "Python", "Python", "java", "JavaScript", "Javascript", "Go", "Go", ignore_case=False))
