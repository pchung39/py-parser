import io

def parse(text):
    #states
    is_token = False
    previous_character_is_escape = False
    no_quote_value = True
    end_of_line = False

    row_counter = 2

    with io.open(text,'rb',newline=None) as f:
        while 1:
            byte = f.read(1)
            for i in byte:
                if is_token == False:
                    if i == '"':
                        print '\b' + i,
                        print '1'
                        is_token = True
                        no_quote_value = False
                    elif i == '\n':
                        print '\n'
                        print '2'
                    elif i == ',':
                        print '\n' + '\b',
                        print '3'
                    elif no_quote_value == True:
                        print '\b',
                        print '4'
                        is_token = True
                    else:
                        print '\b' + i,
                        print '5'


                elif is_token == True:
                    if i == '\\':
                        print '\b' + i,
                        print '6'
                        previous_character_is_escape = True
                    # for line delimiter
                    elif i == '\n':
                        print '\n'
                        print '7'
                        is_token = False
                    elif previous_character_is_escape == True and i != 'n':
                        print '\b' + i,
                        print '8'
                        previous_character_is_escape = False
                    elif previous_character_is_escape == False and i == '"':
                        print '\b' + i,
                        print '9'
                        is_token = False
                        no_quote_value = True
                    elif no_quote_value == True and i == ',':
                        print '\n' + '\b',
                        print '10'
                        is_token = False
                    elif no_quote_value == False and i == ',':
                        print '\b' + i,
                        print '11'
                    else:
                        print '\b' + i,
                        print '12'

parse('example.csv')
