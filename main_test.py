import io
import os
from os import path
from os.path import basename



#file_base = os.path.basename('"app/csv_upload_directory/%s.csv' % filename)
#new_base = os.path.splitext(file_base)[0]
#file_path = path.relpath("app/csv_upload_directory/%s_result.csv" % new_base)


def parse(text):
    #states
    is_token = False
    previous_character_is_escape = False
    no_quote_value = True
    quote_value = False


    file_base = os.path.basename('"app/csv_upload_directory/%s' % text)
    new_base = os.path.splitext(file_base)[0]
    #file_path = path.relpath("app/csv_upload_directory/%s_result.csv" % new_base)



    row_counter = 1
    token_counter = 0
    fo = open("csv_upload_directory/%s_results.csv" % new_base, "w+")

    fo.write("Row %i" % row_counter + '\n')
    row_counter += 1
    with io.open(text,'rb',newline=None) as f:
        while True:
            byte = f.read(1)
            for i in byte:
                #print "%s,%s" % (no_quote_value,previous_character_is_escape)
                if is_token == False:
                    if i == '"':
                        fo.write(i)
                        token_counter = 0
                        is_token = True
                        no_quote_value = False
                        quote_value = True
                    elif i == '\n':
                        fo.write(" ")
                        fo.write("(%i)" % token_counter)
                        fo.write('\n')
                        fo.write("Row %i" % (row_counter))
                        fo.write("\n")
                        token_counter = 0
                        row_counter += 1
                    elif i == ',':
                        fo.write(" ")
                        fo.write("(%i)" % token_counter)
                        fo.write('\n')
                        token_counter = 0
                    elif no_quote_value == True:
                        fo.write(i)
                        token_counter += 1
                        is_token = True
                        quote_value = False
                    else:
                        fo.write(i)
                        token_counter += 1


                elif is_token == True:
                    # start of an escape sequence
                    if i == '\\':
                        fo.write(i)
                        token_counter += 1
                        previous_character_is_escape = True
                    # for line delimiter, the quoted values are being processed outside token
                    elif no_quote_value == True and i == '\n':
                        fo.write(" ")
                        fo.write("(%i)" % token_counter)
                        fo.write('\n')
                        fo.write("Row %i" % (row_counter))
                        fo.write("\n")
                        token_counter = 0
                        row_counter += 1
                        is_token = False
                    # if token is not a quoted value but ends with quotes, and there is no escape character
                    elif no_quote_value == True and previous_character_is_escape == False and i == '"':
                        fo.write(i)
                        fo.write("This is a not a valid token, this is not a quoted value but there is an ending quote")
                        return False
                    # builds off previous_character_is_escape and captures any escape sequence
                    elif previous_character_is_escape == True:
                        fo.write(i)
                        token_counter += 1
                        previous_character_is_escape = False
                    # this type of quote is the end of token, returns back to other if statement
                    elif previous_character_is_escape == False and i == '"':
                        fo.write(i)
                        no_quote_value = True
                        quote_value = False
                        is_token = False
                    # if token starts as a quote but ends without quotes
                    elif quote_value == True and previous_character_is_escape == False and i == ',':
                        fo.write(i)
                        fo.write("This is not a valid token, there should be a quote at the end of this token")
                        return False
                    # this comma marks the end of a non quoted token, this invokes a newline
                    elif no_quote_value == True and previous_character_is_escape == False and i == ',':
                        fo.write(" ")
                        fo.write("(%i)" % token_counter)
                        fo.write('\n')
                        token_counter = 0
                        is_token = False
                    elif no_quote_value == False and i == ',':
                        fo.write(i)
                        fo.write("DONG")
                    else:
                        fo.write(i)
                        token_counter += 1
        fo.close()
        f.close()

parse('example.csv')

'''
    print "This is row %i" % (row_counter)
    row_counter += 1
    with io.open(file_path,'rb',newline=None) as f:
        while True:
            byte = f.read(1)
            for i in byte:
                #print "%s,%s" % (no_quote_value,previous_character_is_escape)
                if is_token == False:
                    if i == '"':
                        print '\b' + i,
                        is_token = True
                        no_quote_value = False
                        quote_value = True
                    elif i == '\n':
                        print '\n'
                        print "This is row %i" % (row_counter)
                        row_counter += 1
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
                    # for line delimiter, the quoted values are being processed outside token
                    elif no_quote_value == True and i == '\n':
                        print '\n'
                        print "This is row %i" % (row_counter)
                        row_counter += 1
                        is_token = False
                    # if token is not a quoted value but ends with quotes, and there is no escape character
                    elif no_quote_value == True and previous_character_is_escape == False and i == '"':
                        print '\b' + i,
                        print "(This is a not a valid token, this is not a quoted value but there is an ending quote)"
                        return False
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
                    # if token starts as a quote but ends without quotes
                    elif quote_value == True and previous_character_is_escape == False and i == ',':
                        print '\b' + i,
                        print "(This is not a valid token, there should be a quote at the end of this token)"
                        return False
                    # this comma marks the end of a non quoted token, this invokes a newline
                    elif no_quote_value == True and previous_character_is_escape == False and i == ',':
                        print '\n' + '\b',
                        is_token = False
                    elif no_quote_value == False and i == ',':
                        print '\b' + i,
                    else:
                        print '\b' + i,

'''
