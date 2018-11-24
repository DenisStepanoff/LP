class hello:

	def input_name():
		name = input()
		if name == '':
		    return 'NoName'
		return name

	def hello_name(name):
		print(f"Привет {name}")


def main():
	name = hello.input_name()
	hello.hello_name(name)


if __name__ == '__main__':
 	main()
