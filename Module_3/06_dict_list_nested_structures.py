workers = [
    {'id': 1, 'job_title': 'junior_developer', 'name': 'John', 'programming_language': ['python']},
    {'id': 2, 'job_title': 'senior_developer', 'name': 'Mark', 'programming_language': ['python', 'php']},
    {'id': 3, 'job_title': 'stuff_developer', 'name': 'Alex', 'programming_language': ['python', 'php', 'javascript']},
    {'id': 4, 'job_title': 'junior_developer', 'name': 'john', 'programming_language': ['javascript', 'php']},
    {'id': 5, 'job_title': 'Senior_developer', 'name': 'Carl', 'programming_language': ['python', 'javascript']},
    {'id': 5, 'job_title': 'junior_developer', 'name': 'Martha', 'programming_language': ['python']},
]

programming_stat = {}

for worker in workers:
    for programming_language in worker['programming_language']:
        if programming_language not in programming_stat:
            programming_stat[programming_language] = {
                'quantity': 0,
                'names': []
            }

        programming_stat[programming_language]['quantity'] += 1
        programming_stat[programming_language]['names'].append(worker['name'])

# Print stat - how much popular is specific programming language in team
print(f'Programming statistics: {programming_stat}')