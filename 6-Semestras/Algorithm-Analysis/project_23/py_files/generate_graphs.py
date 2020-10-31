#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com, marius.pozniakovas@mif.stud.vu.lt"
'''script for 23rd task of Algorithm Analysis'''

import matplotlib.pyplot as plt

data_era = {
    "Number":[],
    "Time":[] 
}

data_miller = {
    "Number":[],
    "Time":[],
    "Iterations":[]
}

def append_data(algorithm, number, time_needed, iterations = None):
    if algorithm == '1':
        data_era['Number'].append(number)
        data_era['Time'].append(time_needed)
    elif algorithm == '2':
        data_miller['Number'].append(number)
        data_miller['Time'].append(time_needed)
        data_miller['Iterations'].append(iterations)
    
    return

def order_data(algorithm):

    if algorithm == '1':
    
        list1 = data_era['Number']
        list2 = data_era['Time']
        
        list1, list2 = zip(*sorted(zip(list1, list2)))
        
        data_era['Number'] = list1
        data_era['Time'] = list2

    elif algorithm == '2':
        list1 = data_miller['Number']
        list2 = data_miller['Time']
        list3 = data_miller['Iterations']

        list1, list2, list3 = zip(*sorted(zip(list1, list2, list3)))

        data_miller['Number'] = list1
        data_miller['Time'] = list2
        data_miller['Iterations'] = list3

    return

def generate_graph(algorithm, x_axis, y_axis):
    
    if algorithm == '1':
        plt.plot(data_era['Number'], data_era['Time'], color = 'black')
        plt.suptitle('Eratosthenes algorithm')
    elif algorithm == '2':
        plt.plot(data_miller['Number'], data_miller['Time'], color = 'black')
        plt.suptitle('Miller-Rabin algorithm')
    
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()
    
def get_data_len(algorithm):
    if algorithm == '1':
        return len(data_era['Number'])
    elif algorithm == '2':
        return len(data_miller['Number'])

