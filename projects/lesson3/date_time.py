from datetime import datetime, timedelta

date_string = '01/01/17 12:10:03.234567'

def day_shift(num_days):
	return (datetime.now() + timedelta(days=num_days))

if __name__ == '__main__':
	
    print(day_shift(-1))
    print(day_shift(0))
    print(day_shift(-30))

    print(datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f'))
