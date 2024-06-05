# Adding new emails and removing dupliactes

emails_list = ['mail1@gmail.com', 'mail2@gmail.com', 'mail1@gmail.com', 'mail2@gmail.com', 'mail2@gmail.com',
               'mail3@gmail.com''mail4@gmail.com',
               'mail331@gmail.com', 'mail2@gmail.com', 'mail12@gmail.com', 'mail11@gmail.com''mail44@gmail.com']
print(len(emails_list))

for i in range(5):
    print('- - - ' * 5)
    email = input(f'Write email adress - {i + 1} of 5 - ')
    if '@' in email and (email.endswith('.com') or email.endswith('.pl')):
        emails_list.append(email)
        print('Mail added')
    else:
        print(f'{email} is incorrect email')

print('- - - ' * 5)
print(f'Number of mails before removing dupliactes: {len(emails_list)}')
print(f'Number of mails after removing dupliactes: {len(set(emails_list))}')
