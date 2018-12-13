import re
import csv


class SquidAccessLogParser:

    def __init__(self, log_file_name, csv_file_name):
        self.log_file = open(log_file_name, 'r')
        self.csv_file = open(csv_file_name, 'w')
        self.csv_fields = ['utime', 'elapsed', 'client', 'bytes', 'method', 'url', 'ident', 'mimetype']


    def __del__(self):
        self.log_file.close()
        self.csv_file.close()

    def __row_parse(self, row):
        split_row = re.split(" {1,6}", row)

        line_in_dict = {
        'utime': int(float(split_row[0])),
        'elapsed': int(split_row[1]),
        'client': split_row[2],
        'bytes': int(split_row[4]),
        'method': split_row[5],
        'url': split_row[6],
        'ident': split_row[7],
        'mimetype': split_row[9]
        }
        
        return line_in_dict

    def get_csv(self):
        writer = csv.DictWriter(self.csv_file, self.csv_fields, delimiter=';')
        writer.writeheader()
        for log_line in self.log_file:
            writer.writerow(self.__row_parse(log_line))



def main():

    #pass
    parser = SquidAccessLogParser('access.log', 'parsed.csv')
    parser.get_csv()


if __name__ == '__main__':
    main()
