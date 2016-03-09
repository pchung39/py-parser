import io


def parse(text):
    #states
    is_token = False
    previous_character_is_escape = False
    no_quote_value = True
    quote_value = False

    # fancy pants row counter
    row_counter = 2

    with io.open(text,'rb',newline=None) as f:
        while True:
            byte = f.read(1)
            for i in byte:
                print "%s,%s" % (quote_value,no_quote_value)
                if is_token == False:
                    if i == '"':
                        print '\b' + i,
                        is_token = True
                        no_quote_value = False
                        quote_value = True
                    elif i == '\n':
                        print '\n'
                    elif i == ',':
                        print '\n' + '\b',
                    elif no_quote_value == True:
                        print '\b' + i,
                        is_token = True
                        quote_value = False
                    else:
                        print '\b' + i,


                elif is_token == True:
                    # start of an escape sequence
                    if i == '\\':
                        print '\b' + i,
                        previous_character_is_escape = True
                    # for line delimiter
                    elif i == '\n':
                        print '\n'
                        print "This is row %i" % (row_counter)
                        row_counter += 1
                        is_token = False
                    # builds off previous_character_is_escape and captures any escape sequence
                    elif previous_character_is_escape == True:
                        print '\b' + i,
                        previous_character_is_escape = False
                    # this type of quote is the end of token, returns back to other if statement
                    elif previous_character_is_escape == False and i == '"':
                        print '\b' + i,
                        no_quote_value = True
                        quote_value = False
                        is_token = False
                    # rework this state, this is the same as two loops below
                    elif no_quote_value == True and previous_character_is_escape == False and i == ',':
                        print '\n' + "This is not a valid token"
                        return False
                    # if token starts as a quote but ends without quotes
                    elif quote_value == True and previous_character_is_escape == False and i == ',':
                        print '\n' + "This is not a valid token"
                        return False
                    # differentiating between commas that should be considered part of the string and those that should not be
                    elif no_quote_value == True and i == ',':
                        print '\n' + '\b',
                        no_quote_value = False
                        is_token = False
                    elif no_quote_value == False and i == ',':
                        print '\b' + i,
                    else:
                        print '\b' + i,

parse('example.csv')
