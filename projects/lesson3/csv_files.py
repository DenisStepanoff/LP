import csv

users = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        ]

with open('users.csv', 'w', encoding='utf-8', newline='') as csv_file:
	fields = ['name', 'age', 'job']
	writer = csv.DictWriter(csv_file, fields, delimiter=';')
	writer.writeheader()
	for user in users:
		print(user)
		writer.writerow(user)

