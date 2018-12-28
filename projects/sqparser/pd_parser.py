import pandas as pd
import requests


delimiter = '\s+'                         # delimiter in log file
chunk_size = 15                           # memory saving with chunk read; in prod chunk_size=20000
log_file_name = 'access.log'          # log file path
csv_file_name = 'parsed.csv'              # csv file path
url = 'http://127.0.0.1:8000/file/upload/'# url in django rest framework

# parse log file and create csv file with parsed data
def get_csv(log_file_name, csv_file_name):

    data_frame = pd.read_csv(log_file_name, sep=delimiter, header=None, chunksize=chunk_size)
    for chunk in data_frame:
      chunk.to_csv(csv_file_name, header=None, mode='a') # mode='a' - append mode

# upload csv into django web site with django REST framework 
def upload_file(csv_file_name):
    
    with open(csv_file_name, 'rb') as upload_file_handle:
        files = {'file': upload_file_handle}
        r = requests.post(url, files=files)

# main program
def main():

    get_csv(log_file_name, csv_file_name)
    #upload_file(csv_file_name)


if __name__ == '__main__':
    main()