things = {'sword', 'shield', 'bow', 'armor'}

# checking_thing = 'sword'
checking_thing = 'knife'

if checking_thing in things:
    print(f'He have a {checking_thing}')
else:
    things.add(checking_thing)
    print(f'{checking_thing} is added! Full list: {things}')
