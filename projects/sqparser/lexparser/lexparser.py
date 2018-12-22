import re
import sys
import datetime
import logging

class AccessLogParser:

    def __init__(self, log_file_name, csv_file_name):

        #TODO: kick LOG_FIELDS, RE_RULES, LOG_FIELDS and tokern_type values in separate config file
        self.LOG_FIELDS = ('utime', 'elapsed', 'client', 'response', 'bytes', 'method', 'url', 'ident', 'hierarchy', 'mimetype')
        self.DELIMITER, self.DATE, self.RAW, self.EMPTY_DATA = range(4)
        self.RE_RULES = [
            ('\s+', self.DELIMITER),
            ('-|"-"', self.EMPTY_DATA),
            ('([^\s]+)', self.RAW),
            ]
        self.LOG_FIELDS = ('utime', 'elapsed', 'client', 'response', 'bytes', 'method', 'url', 'ident', 'hierarchy', 'mimetype')
        self.log_file_name = log_file_name
        self.csv_file_name = csv_file_name


    def __lexic_analyzer(self, rules):

        re_prep = [(re.compile(regexp), token_type) for regexp, token_type in rules]

        def __lex(line):
            stop_position = len(line) 
            current_position = 0          
            while current_position < stop_position:
                for pattern, token_type in re_prep:  
                    match = pattern.match(line, current_position)    
                    if match is None:                 
                        continue
                    current_position = match.end()                  
                    yield (match, token_type)         
                    break                            
            
        return __lex


    def __syntax_analyzer(self, line):

        lexer = self.__lexic_analyzer(self.RE_RULES)
        tokens = lexer(line)
        field_index = 0

        for re_match, token_type in tokens:
            
            if token_type == self.DELIMITER:
                continue  
            elif token_type ==  self.EMPTY_DATA:
                value = None  # 
            elif token_type == self.RAW:
                value = re_match.group(1) 
            else:
                raise SyntaxError("Unknown token", token_type, re_match)

            field_name = self.LOG_FIELDS[field_index]
            field_index += 1

            print('{},{}'.format(field_name, value))


    def get_csv(self):

        with open(self.log_file_name, 'r') as logfile:

            for line in logfile:
                self.__syntax_analyzer(line)
                print('---------------------------------------------')


def main():
    
    parser = AccessLogParser('access.log', 'parsed.csv')
    parser.get_csv()

if __name__ == '__main__':
    main()

