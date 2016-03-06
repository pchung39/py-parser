
def parse(text):
    #states
    is_token = False
    previous_character_is_escape = False
    no_quote_value = True

    with open(text) as f:
        for l in f:
            for i in l:
                #print '%s,%s,%s' % (is_token,previous_character_is_escape,no_quote_value)
                if is_token == False:
                    if i == '"':
                        print '\b' + i,
                        print "1"
                        is_token = True
                        no_quote_value = False
                    elif i == ',':
                        print '\n',
                        print "2"
                    elif no_quote_value == True:
                        print '\b' + i,
                        print "3"
                        is_token = True
                    else:
                        print '\b' + i,
                        print "4"

                elif is_token == True:
                    if i == '\\':
                        print '\b' + i,
                        print "5"
                        previous_character_is_escape = True
                    elif previous_character_is_escape == True and i == '"':
                        print '\b' + i,
                        print "5"
                        previous_character_is_escape = False
                    elif previous_character_is_escape == False and i == '"':
                        print '\b' + i,
                        print "5"
                        is_token = False
                        no_quote_value = True
                    elif no_quote_value == True and i == ',':
                        print '\n',
                        print "6"
                        is_token = False
                    elif no_quote_value == False and i == ',':
                        print '\b' + i,
                        print "7"
                    else:
                        print '\b' + i,
                        print "8"
parse('example.csv')
