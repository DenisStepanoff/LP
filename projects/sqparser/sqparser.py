
import re

class SquidParser:

    def __init__(self):
        pass

    def row_parse(self, row):

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

def main():
    with open('access.log', 'r') as log_file:
        parser = SquidParser()
        for log_line in log_file:
            print(parser.row_parse(log_line))

if __name__ == '__main__':
    main()
