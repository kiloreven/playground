#! /bin/python
import re

def find_type_and_cast_to_string(input):
    if isinstance(input, (int, float)):
        if isinstance(input, float):
            input = int(input)

        output = unicode(input)
        output_type = 'dec'

    elif isinstance(input, (str, unicode)):
        if re.match(input.upper(), '[A-F]'):
            output = re.sub(':', '', unicode(input.upper()))
            output_type = 'hex'
        elif not input.isdigit():
            output = None
            output_type = 'err' 
        else:
            output = unicode(input)
            output_type = 'dec'
    else:
        output = None
        output_type = 'err' 

    return output, output_type


def prompt():
    user_input = raw_input('\nScan a device on an NFC/RFID HID reader:  ')

    value, type = find_type_and_cast_to_string(user_input)

    print '\n== ANALYSIS =='
    print 'Type: %s\nInput: %s\nWashed input: %s' % (type, user_input, value)

    prompt()

prompt()
