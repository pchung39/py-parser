import io
import sys


def parse(file):
    #states
    is_token = False
    previous_character_is_escape = False
    no_quote_value = True
    end_of_line = False

    row_counter = 2

    with io.open(file,'rb',newline=None) as f:
        while 1:
            byte = f.read(1)
            for i in byte:

                if is_token == False:

                    if i == '"':
                        print '\b' + i,

                        is_token = True
                        no_quote_value = False

                    elif i == '\n':
                        print '\n'

                    elif i == ',':
                        print '\n' + '\b',

                    elif no_quote_value == True:
                        print '\b' + i,
                        is_token = True

                    else:
                        print '\b' + i,

                elif is_token == True:
                    if i == '\\':
                        print '\b' + i,
                        previous_character_is_escape = True

                    # for line delimiter
                    elif i == '\n':
                        print '\n'
                        is_token = False

                    elif previous_character_is_escape == True and i != 'n':
                        print '\b' + i,
                        previous_character_is_escape = False

                    elif previous_character_is_escape == False and i == '"':
                        print '\b' + i,
                        is_token = False
                        no_quote_value = True

                    elif no_quote_value == True and i == ',':
                        print '\n' + '\b',
                        is_token = False

                    elif no_quote_value == False and i == ',':
                        print '\b' + i,

                    else:
                        print '\b' + i,

if __name__ == "__main__":
    file = raw_input("File name (must be in csv format): ")
    split_file = file.split(".")

    if len(split_file) == 1 or file.split(".")[1] != "csv":
        print "The file was not in csv format."
    else:
        parse(file)
