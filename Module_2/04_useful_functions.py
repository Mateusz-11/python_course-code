remarks = (4, 6, 5, 4, 3, 3, 6, 6, 6, 6, 6)

print(sorted(remarks))
print('- - - - -')

print(sum(remarks) / len(remarks))

if sum(remarks) / len(remarks) >= 4.75:
    print('Pupil`ll get a certificate with stripe')
else:
    print('Pupil`ll not get a certificate with stripe')
