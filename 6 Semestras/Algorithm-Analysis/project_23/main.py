#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com, marius.pozniakovas@mif.stud.vu.lt"
'''script for 23rd task of Algorithm Analysis'''

#my own files
import py_files.prime_test as pt
import py_files.file_operations as fo
import py_files.generate_graphs as gg

#for sys argv
from sys import argv

mode = argv[1].lower()

if mode == 'file':

    #read data from numbers
    numbers = fo.read_data_from_numbers()

    #output file creation and file_name
    output_file, file_name = fo.create_file_for_output()

    #READING FROM FILE HERE
    for testing_for_prime in numbers:
        elements = testing_for_prime.split(';')
        if len(elements) > 2:
            prime, time = pt.check_if_number_is_prime(check_if_prime = int(elements[0]), algorithm = elements[1], iterations_for_miller_rabin = int(elements[2]))
            fo.output_to_file(is_prime = prime, number = elements[0], algorithm = elements[1], out_file = output_file, iterations = int(elements[2]), time = time)
        else:
            prime, time = pt.check_if_number_is_prime(check_if_prime = int(elements[0]), algorithm = elements[1])
            fo.output_to_file(is_prime = prime, number = elements[0], algorithm = elements[1], out_file = output_file, time = time)

        #for graph generation
        gg.append_data(algorithm = str(elements[1]), number = int(elements[0]), time_needed = time)

    fo.close_file(output_file, file_name)

    for i in ['1', '2']:
        if gg.get_data_len(i) > 0:
            gg.order_data(i)
            gg.generate_graph(algorithm = i, x_axis = 'Numbers', y_axis = 'Time (seconds)')

elif mode == 'test':
    file1 = open('files/eratosthenes.txt', 'w+')
    #algorithm 1
    for i in range(1, 10001):
        prime, time = pt.check_if_number_is_prime(check_if_prime = int(i), algorithm = '1')
        fo.output_to_file(is_prime=prime, number=i, algorithm='1', out_file=file1, time = time)
        gg.append_data(algorithm = '1', number = i, time_needed = time)
    file1.close()
    

    file2 = open('files/miller_rabin.txt', 'w+')
    #algorithm 2
    for i in range(1, 10001):
        for k in [10, 20, 50, 100, 200]:
            prime, time = pt.check_if_number_is_prime(check_if_prime = int(i), algorithm = '2', iterations_for_miller_rabin=k)
            fo.output_to_file(is_prime=prime, number=i, algorithm='2', out_file=file2, iterations=k, time = time)
            gg.append_data(algorithm = '2', number = i, time_needed = time)
    file2.close()

    #order and show graphs
    gg.order_data('1')
    gg.generate_graph(algorithm = '1', x_axis = 'Numbers', y_axis = 'Time (seconds)')
    gg.order_data('2')
    gg.generate_graph(algorithm = '2', x_axis = 'Numbers', y_axis = 'Time (seconds)')

else:
    quit('usage main.py [test/file]')
                
            