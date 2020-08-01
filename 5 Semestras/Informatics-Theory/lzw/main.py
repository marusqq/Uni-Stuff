#!/usr/bin/env python
__author__ = "Marius Pozniakovas, Tomas Kučejevas, Lukas Miežys, Rafal Michalkiewicz"
#main logic for lzw algorithm

import lzw
import sys
import os
import time
from sys import argv

os.system('cls')

startTime = time.time()
TIMER = True
bad_input = False


#validations
if True:

    if argv[1] == 'C':
        
        if len(argv) != 5 or not (argv[4].lstrip('-+').isdigit()):
            bad_input = True
        filename, file_extension = os.path.splitext(argv[3])

    elif argv[1] == 'D':
        if len(argv) != 4:
            bad_input = True
        filename, file_extension = os.path.splitext(argv[2])

    else:
        bad_input = True

    if bad_input:
        sys.exit('Usage python [main.py] [C/D (C for Compressing, D for Decompressing)] [file_to_use.extension] [file_to_compress/decompress_to.extension] [m number[only for encoding]]')

try:
    #compressing:
    if argv[1] == 'C':

        #0.1 we will be using /files/ and /compressed/
        input_dir = 'files/'
        compress_dir = 'compressed/' 

        #1.1 get full dir of input_file
        input_dir = input_dir + argv[2]

        #1.2 read byte stream from input_dir
        print ('Reading ' + input_dir + '...', end = '\t')
        infile = lzw.readbytes(input_dir)
        print ('Done')

        #1.3 compress data from byte stream
        #print ('Compressing data...', end = '\t')
        compressed = lzw.compress(infile)
        #print ('Done')

        #2.1 get full dir of compressed_files
        compress_file = compress_dir + argv[3]

        #2.2 write compressed data to compressed_files
        print ('Writing compressed data to ' + compress_file + '...', end = '\t')
        lzw.writebytes(compress_file, compressed)
        print ('Done')   
    #--------------------------------------------------------

    #decompressing:
    elif argv[1] == 'D':
 
        #0.1 we will be using /decompressed/ and /compressed/
        decompress_dir = 'decompressed/'
        compress_dir = 'compressed/'

        #3.1 get full dir of compressed_files
        compress_dir = compress_dir + argv[2]

        #3.2 read from compressed_dir
        print ('Reading ' + compress_dir + '...', end = '\t')
        infile = lzw.readbytes(compress_dir)
        print ('Done')

        #3.3 decompress the bytestream
        #print ('Decompressing data...', end = '\t')
        decompressed = lzw.decompress(infile)
        #print ('Done')

        #4.1 get full dir of decompressed_files
        decompress_file = decompress_dir + argv[3]

        #4.2 write bytestream to decompressed_files_dir
        print ('Writing decompressed data to ' + decompress_file + '...', end = '\t')
        lzw.writebytes(decompress_file, decompressed)
        print ('Done')

    #close file debug.log
    lzw.debug(text = 'TERMINATE')

    if TIMER:
        loadingTime = time.time()
        total = loadingTime - startTime
        print ('Finished. Time: ' + str(total))

except KeyboardInterrupt:
    print('Code interrupted with KeyboardInterrupt')