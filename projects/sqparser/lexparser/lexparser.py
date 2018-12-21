import re
import sys
import datetime
import logging

DELIMITER, DATE, RAW, EMPTY_DATA = range(4) #   todo replase strukt

RE_RULES = [
    ('\s+', DELIMITER),
    ('-|"-"', EMPTY_DATA),
    ('([^\s]+)', RAW),
    ]

def lexic_analyzer(rules):

    re_prep = [(re.compile(regexp), token_type) for regexp, token_type in rules]

    def lex(line):
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
            
    return lex


class LogEntry(object):
    LOG_FIELDS = ('utime', 'elapsed', 'client', 'response', 'bytes', 'method', 'url', 'ident', 'hierarchy', 'mimetype')
    

lexer = lexic_analyzer(RE_RULES)

with open('access.log', 'r') as logfile:

    for line in logfile:  
        try:
            tokens = lexer(line)
        except Exception:
            logging.exception("Error in line '%s'", line)
            continue  
        entry = LogEntry()
        field_index = 0

        #print(LogEntry.FIELDS[field_idx])
        #print(tokens)

        for re_match, token_type in tokens:
            #print(re_match)
            #print(token_type)

            
            if token_type == DELIMITER:
                continue  
            elif token_type ==  EMPTY_DATA:
                value = None  # 
            elif token_type == RAW:
                value = re_match.group(1) 

            else:
                raise SyntaxError("Unknown token", token_type, re_match)

            #print(field_idx)
            #print('TT')

            field_name = LogEntry.LOG_FIELDS[field_index]
            setattr(entry, field_name, value)
            field_index += 1
        print (entry.utime, entry.url, entry.bytes, entry.client)
