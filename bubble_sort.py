# -*- coding: utf-8 -*-
import os
import csv
import cProfile

d = []

def make_list(my_list):
    with open("csv_upload_directory/%s.csv" % my_list, 'r') as file:
        file_lines = csv.reader(file)
        for i in file_lines:
            for w in i:
                d.append(w)

def bubble_sort(sortable):
    # constraints on token list length
    for i in range(len(sortable)):
        # in order to compare two token lengths, this for loop must start one token from the beginning, hence (i + 1). It also uses the same length contraints
        for j in range(i+1, len(sortable)):
            # this compares first token length with second token length.
            if len(sortable[j]) < len(sortable[i]):
                # if if clause is met, swap the two tokens. and move on
                sortable[j], sortable[i] = sortable[i], sortable[j]
    sortable = d
    write_file(sortable, "example_results")

def write_file(file, filename):
    with open("csv_upload_directory/%s.csv" % filename, 'w') as csv:
        for d in file:
            csv.write(d)
            csv.write('\n')
    csv.close()

make_list('example_results')
bubble_sort(d)

# nums = list(sortable)