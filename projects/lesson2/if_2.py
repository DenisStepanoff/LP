def string_compare(str1, str2):
	
	_out = []
	if not (isinstance(str1, str) and isinstance(str2, str)):
		_out.append(0)
		return _out
	elif str1 == str2:
		_out.append(1)
		return _out
	elif str1 != str2:
		if len(str1) > len(str2):
			_out.append(2)
		if str2 == 'learn':
			_out.append(3)
		return _out


print(string_compare(1,2))
print(string_compare('qwerty','qwerty'))
print(string_compare('12345','123'))
print(string_compare('123','learn'))
print(string_compare('123456789','learn'))
print(string_compare('',''))


