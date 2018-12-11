class SquidLogParser:
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name

    def iter_line(self):
        with open(log_file_name, 'r') as iter_file:
            if log_line in iter_file:
                yield log_line


def main():
    parser = SquidLogParser('access.log')
    print(parser.iter_line())

if __name__ == '__main__':
    main()


