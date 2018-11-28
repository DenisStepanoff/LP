def get_sum(num_one, num_two):
    try:
        num_one = int(num_one)
        num_two = int(num_two)
    except ValueError:
        print('Функция принимает только числа или значания приводимые к типу int')
        return
    return num_one + num_two


if __name__ == '__main__':

    print(get_sum(1, 2)) #3
    print(get_sum('qwe', 'rty')) #except
    print(get_sum('1', 2)) #3
    print(get_sum('qwe', 2)) #except
    print(get_sum(1.2, 2.3)) #3
    print(get_sum('1.2', '2.3')) #except
