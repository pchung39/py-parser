string = '"age","coun,try","location"'

token_begin = False
token_end = False
is_string = False

print string + '\n'

def parse(input, token_begin, token_end, is_string):
    for i in string:
        if i == '"':
            return token_begin == True
            return is_string == False
            print '\b' + i,
        elif i != '"':
            return is_string == True
            print '\b' + i,
        elif i == ',' and token_begin == True:
            print '\b',
        #elif i == '"':
            #pass
        elif i == '"' and token_begin == True and is_string == True:
            return token_end == True
            print '\b' + i,
            print '\n'

print parse(string,False,False,False)
