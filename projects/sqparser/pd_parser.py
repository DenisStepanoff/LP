import pandas as pd
import requests

DELIMETER = '\s+'
CHUNK_SIZE = 15


def chunck_generator(log_file_name, header=False, chunk_size=CHUNK_SIZE):

   for log_chunk in pd.read_csv(log_file_name, delimiter=DELIMETER, iterator=True, chunksize=chunk_size): 
        yield log_chunk


def row_generator(log_file_name, header=False, chunk_size=CHUNK_SIZE):

    log_chunk = chunck_generator(log_file_name, header=False, chunk_size=chunk_size)
    for row in log_chunk:
        yield row



def main():

    log_file_name = 'access.log'
    gen_row = row_generator(log_file_name=log_file_name)
    while True:
        print(next(gen_row))


if __name__ == '__main__':
    main()