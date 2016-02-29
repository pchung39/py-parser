'''
string = '"age",",coun\,try,","location"'


#is_string = False

print string

def parse(token):
    token_begin = False
    token_end = False

    for i in token:
        if token_begin == False:
            if i == '"':
                token_begin = True
                token_end = False
            elif i == ',':
                print '\n'
        else:
            if i != '"':
                print i,
            else:
                token_begin = False
                token_end = True
        #if i == '"' and token_begin == False:
            #print '\b' + i,
            #token_begin == True
        #elif i != '"' and i != ',':
            #print '\b' + i,
            #is_string == True
        #elif i == ',' and is_string == True:
            #print '\b' + i,
        #elif i == '"':
            #pass
        #elif i == '"' and token_begin == True and is_string == True:
            #print '\b' + i,
            #token_end == True
        #elif i == ',' and token_end == True:
            #print '\b' + '\n'

print parse(string)
'''

string = r'"age",ab\"c,123,",coun\",try,","location"'

def parse(token):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    is_token = False
    previous_character_is_escape = False
    print_statement = '\b' + i,
    for i in token:
        #print '%s,%s' % (is_token,previous_character_is_escape)
        if is_token == False:
            if i == '"':
                print '\b' + i,
                is_token = True
            elif i == numbers:
                print '\b' + i,
                is_token = True
            elif i == ',':
                print '\n',
            else:
                print '\b' + i,

        elif is_token == True:
            if i == '\\':
                print '\b' + i,
                previous_character_is_escape = True
            elif previous_character_is_escape == True and i == '"':
                print '\b' + i,
                previous_character_is_escape = False
            elif previous_character_is_escape == False and i == '"':
                print '\b' + i,
                is_token = False
            elif i == ',':
                print '\b' + i,
                is_token = False
            else:
                print '\b' + i,
parse(string)
