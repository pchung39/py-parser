import io
#string = r'"age",....ab\"c,(-1.2.3.),",c.o.u.n\",try,","location"'
#string = r'"---------",<img src=x onerror=\x32"javascript:alert(1)">'


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
                        is_token = True
                        no_quote_value = False
                    elif i == '\n':
                        print '\n'
                    elif i == ',':
                        print '\n',
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
                        print '\n',
                        is_token = False
                    elif no_quote_value == False and i == ',':
                        print '\b' + i,
                    else:
                        print '\b' + i,

parse('example.csv')
