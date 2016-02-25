string = '"age",",coun\",try,","location"'


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
