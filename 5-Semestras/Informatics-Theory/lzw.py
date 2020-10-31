#!/usr/bin/env python
__author__ = "Marius Pozniakovas, Tomas Kučejevas, Lukas Miežys, Rafal Michalkiewicz"
#LZW file encoder

import sys
from sys import argv
from struct import *
import base64

def setup():

    # taking the input file and the number of bits from command line
    # defining the maximum table size
    # opening the input file
    # reading the input file and storing the file data into data variable

    #Validation for system variables
    if len(argv) < 4 or int(argv[3]) < 2 or int(argv[3]) > 16 or (argv[1] != 'C' and argv[1] != 'D'):
        sys.exit('Usage: python [lzw.py] [C/D (C for compressing, D for decompressing)] [file] [group (2-16)]')

    #file and group number
    input_file, n = argv[2:]

    if argv[1] == 'C':
        compressing = 'Y'
    elif argv[1] == 'D':
        compressing = 'N'
    
    #Get max table size calculated
    maximum_table_size = pow(2,int(n))

    return compressing, input_file, n, maximum_table_size

def decompressing(input_file, n, maximum_table_size):

    file = open(input_file, "rb")
    compressed_data = []
    next_code = 256
    decompressed_data = ""
    string = ""

    # Reading the compressed file.
    while True:
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data, ) = unpack('>H', rec)
        compressed_data.append(data)

    # Building and initializing the dictionary.
    dictionary_size = 256
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

    # iterating through the codes.
    # LZW Decompression algorithm
    for code in compressed_data:
        if not (code in dictionary):
            dictionary[code] = string + (string[0])
        decompressed_data += dictionary[code]
        if not(len(string) == 0):
            dictionary[next_code] = string + (dictionary[code][0])
            next_code += 1
        string = dictionary[code]

    # storing the decompressed string into a file.
    out = input_file.split(".")[0]
    output_file = open(out + "_decompressed.txt", "w")
    for data in decompressed_data:
        output_file.write(data)
        
    output_file.close()
    file.close()
    print ('Decompressing succesful')

def compressing(input_file, n, maximum_table_size):

    #open the file and get data
    #with open(input_file, "rb") as imageFile:
    #data = base64.b64encode(imageFile.read())
    #print (data)
    if input_file.endswith('.txt'):
        file = open(input_file)                 

    else:
        file = open(input_file, 'rb')
    
    data = file.read()


    # Building and initializing the dictionary.
    dictionary_size = 256                   
    dictionary = {chr(i): i for i in range(dictionary_size)}

    string = ""             # String is null.
    compressed_data = []    # variable to store the compressed data.

    # iterating through the input symbols.
    # LZW Compression algorithm
    for symbol in data:                     
        string_plus_symbol = str(string) + str(symbol) # get input symbol.
        if string_plus_symbol in dictionary: 
            string = string_plus_symbol
        else:
            compressed_data.append(dictionary[string])
            if(len(dictionary) <= maximum_table_size):
                dictionary[string_plus_symbol] = dictionary_size
                dictionary_size += 1
            string = symbol

    if string in dictionary:
        if string.isalpha():
            compressed_data.append(dictionary[string])

    # storing the compressed string into a file (byte-wise).
    out = input_file.split(".")[0]
    output_file = open(out + ".lzw", "wb")
    for data in compressed_data:
        #data = data.replace('\x00', '')
        output_file.write(pack('>H',int(data)))
        
    output_file.close()
    file.close()

    print ('Compressing succesful')


#get data to know what to do
used_data = setup()

#now compress or decompress accordingly
if used_data[0] == 'Y':
    compressing(used_data[1], used_data[2], used_data[3])

else:
    decompressing(used_data[1], used_data[2], used_data[3])