#Создайте список, содержащий числа от 2 до 7 ...

l = []

for i in range(2, 8):
    l.append(i)

print(l)
l.append('Python')
print(f'Length: {len(l)}')
print(f'First: {l[0]}')
print(f'Last: {l[-1]}')
print(l[1:4])
l.remove('Python')
#print(l)

#Создайте такой словарь: ...

d = {'city': "Moscow", 'temperature': '20'}
print(d.get('city'))
d['temperature'] = str(int(d['temperature']) - 5)
print(d)
#print(d.__contains__('country'))
# "in" usage:
print('country' in d)
print(d.get('country', 'Russia'))
d['date'] = '27.05.2017'
#print(l)
print(len(d))
