import sys, os
import csv
import tokenize
import cStringIO



# replace with system argv
# csvfile = open("example.csv")

string = '"name","jim","john","tom"'
# function to get next string
def get_next_target(page):
    start_link = page.find('"')
    if start_link == -1:
        return "Invalid String!"
    start_point = page.find('"', start_link)
    end_point = page.find('"', start_point + 1)
    url = page[start_point + 1:end_point]
    return url, end_point

'''
def get_all_target(page):
    while True:

'''

link = get_next_target(string)
print link
