#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com, marius.pozniakovas@mif.stud.vu.lt"
'''script for 23rd task of Algorithm Analysis'''

#for file creation
from datetime import datetime

def read_data_from_numbers():
    '''function used to read from dir/numbers.txt and then returning read data'''

    #import from file, each line is one prime number check
    input_file = open('files/numbers.txt', 'r')
    file_info = input_file.readlines()
    numbers = []

    #add lines that are not starting with #
    for line in file_info:
        if not line.startswith('#') and not line == '\n':
            numbers.append(line.strip('\n'))

    return numbers

def create_file_for_output():
    '''function used to create file called date+time'''

    file_name = str(datetime.now())[:-7]
    #replace spaces with _
    file_name = file_name.replace(' ', '_')
    #replace : with .
    file_name = file_name.replace(':', '.')
    output_file = open('files/'+file_name + '.txt', 'w+')

    return output_file, file_name

def close_file(out_file, file_name):
    '''function just to close and print file_name'''
    print('File ' + file_name + '.txt saved information aswell.')
    out_file.close()

def output_to_file(is_prime, number, algorithm, out_file, time, iterations=None):
    '''function to output prime numbers'''
    
    if is_prime:
        out_file.write(str(number) + ' is PRIME number. Algorithm used: ')
    else:
        out_file.write(str(number) + ' is COMPOSITE number. Algorithm used: ')

    if algorithm == '1':
        out_file.write('Eratosthenes sieve.')
    elif algorithm == '2':
        out_file.write('Miller-Rabin. Iterations used ' + str(iterations) + '. ')

    out_file.write(' Time passed: ' + str(time) + ' secs\n')
