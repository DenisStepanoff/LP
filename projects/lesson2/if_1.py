class UserClassification:
    def input_age():
    	try:
    		age = float(input('Введите свой возраст: '))
    	except ValueError:
    		print('Введенное значение не является числом')
    		return False
    	if age <= 0:
    		print('Ввелено отрицательное число или ноль')
    		return False
    	return age

    def line_of_work(age):
        if age < 6: print('В детский сад')
        elif 6 <= age < 17: print('В школу')
        elif 17 <= age < 22: print('В ВУЗ')
        elif 22 <= age < 65: print('На работу')
        else: print('На пенсию')


age = UserClassification.input_age()
if age != False:
	UserClassification.line_of_work(age)
