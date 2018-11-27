class HelloUser:

	def input_name():
		name = input('Ведите свое имя: ')
		if name == '':
		    return 'NoName'
		return name

	def hello_name(name):
		print(f"Привет {name}")


def main():
	name = HelloUser.input_name()
	HelloUser.hello_name(name)


if __name__ == '__main__':
 	main()
