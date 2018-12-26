import re
import sys
import datetime
import logging
import csv
import requests

class AccessLogParser:

    def __init__(self, log_file_name, csv_file_name):

        #TODO: kick LOG_FIELDS, RE_RULES, LOG_FIELDS and tokern_type values in separate config file
        
        self.DELIMITER, self.DATE, self.RAW, self.EMPTY_DATA = range(4)
        self.RE_RULES = [
            ('\s+', self.DELIMITER),
            ('-|"-"', self.EMPTY_DATA),
            ('([^\s]+)', self.RAW),
            ]
        self.LOG_FIELDS = ('utime', 'elapsed', 'client', 'response', 'bytes', 'method', 'url', 'ident', 'hierarchy', 'mimetype')
        self.log_file_name = log_file_name
        self.csv_file_name = csv_file_name

    # lexic analyzer
    def __lexic_analyzer(self, rules):

        re_prep = [(re.compile(regexp), token_type) for regexp, token_type in rules]  # compile RE

        def __lex(line):  #  function for recursion
            stop_position = len(line) 
            current_position = 0          
            while current_position < stop_position:  
                for pattern, token_type in re_prep:  # try RE one by one
                    match = pattern.match(line, current_position)  # check if the RE matches the string from position current_position
                    if match is None:                # if no match, continue with next RE            
                        continue
                    current_position = match.end()   # shift current position                
                    yield (match, token_type)        # return the found token   
                    break                            # proceed to the analysis of the remaining line
            
        return __lex

    # syntax analyzer
    def __syntax_analyzer(self, line):

        lexer = self.__lexic_analyzer(self.RE_RULES)  # call recursion function
        tokens = lexer(line)                          # start recursion for string lexic analize
        field_index = 0
        line_in_dict = {}

        for re_match, token_type in tokens:           # cicle for syntax analize
            
            if token_type == self.DELIMITER:
                continue                              # skip delimiters
            elif token_type ==  self.EMPTY_DATA:
                value = None                          # EMPTY_DATA replace with None 
            elif token_type == self.RAW:
                value = re_match.group(1)             # return RAW groupp
            else:
                raise SyntaxError("Unknown token", token_type, re_match)  # if unknown token, raise error

            field_name = self.LOG_FIELDS[field_index] # return field name by field index
            field_index += 1

            line_in_dict[field_name] = value          # write parsed data in output dict

            #print('{},{}'.format(field_name, value))

        return line_in_dict

    # file operatios
    def get_csv(self):

        with open(self.log_file_name, 'r') as log_file:
            with open(self.csv_file_name, 'w') as csv_file:
                writer = csv.DictWriter(csv_file, self.LOG_FIELDS, delimiter=';')
                writer.writeheader()

                for line in log_file:
                    writer.writerow(self.__syntax_analyzer(line))
                #print('---------------------------------------------')

# upload csv into django web site with django REST framework
class CommWithRestApi():
 
    def upload_file(file_name):
        url = 'http://127.0.0.1:8000/file/upload/'
        upload_file_handle = open(file_name, 'rb')
        files = {'file': upload_file_handle}
        try:
            r = requests.post(url, files=files)
        finally:
        upload_file_handle.close()


def main():
    
    parser = AccessLogParser('access.log', 'parsed.csv')
    parser.get_csv()

    #upload_file('parsed.csv')

if __name__ == '__main__':
    main()

