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