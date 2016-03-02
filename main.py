import re

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
23,",coun\",try,","location"
'''

string = r'"age",ab\"c,123,",coun\",try,","location"'

def parse(token):
    #regex = re.compile('^[a-zA-Z0-9_]+$')
    is_token = False
    previous_character_is_escape = False
    no_quote_value = False
    for i in token:
        #print '%s,%s,%s' % (is_token,previous_character_is_escape,no_quote_value)
        if is_token == False:
            if i == '"':
                print '\b' + i,
                print "1"
                is_token = True
                no_quote_value == False
            elif i == ',':
                print '\n',
                #print "2"
            elif no_quote_value == True:
                print '\b' + i,
                print "3"
                is_token = True
            else:
                print '\b' + i,
                #print "4"

        elif is_token == True:
            if i == '\\':
                print '\b' + i,
                #print "5"
                previous_character_is_escape = True
            elif previous_character_is_escape == True and i == '"':
                print '\b' + i,
                print "6"
                previous_character_is_escape = False
            elif previous_character_is_escape == False and i == '"':
                print '\b' + i,
                print "7"
                is_token = False
                no_quote_value = True
            elif no_quote_value == True and i == ',':
                print '\n',
                print "8"
                is_token = False
            elif no_quote_value == False and i == ',':
                print '\b' + i,
                print "9"
            else:
                print '\b' + i,
                #print "10"
parse(string)
