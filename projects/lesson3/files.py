file_len = 0
words_num = 0
with open('referat.txt', 'r', encoding='utf-8') as my_file, open('referat2.txt', 'w', encoding='utf-8') as my_file2:
	for file_line in my_file:
		file_len += len(file_line)
		words_num += len(file_line.split(' '))
		my_file2.write(file_line.replace('.', '!'))

print(f'Длина содержимого файла: {file_len}')
print(f'Количество слов: {words_num}')
