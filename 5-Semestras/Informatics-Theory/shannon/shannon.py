# Shannon-Fano Data Compression
# http://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding
# (Max compressible file size: 2**32 bytes)
# FB - 201012153
import sys
import os
import binascii
import math
import collections
import operator

def shannon_fano_encoder(iA, iB): # iA to iB : index interval
    global tupleList
    size = iB - iA + 1
    if size > 1:
        mid = int(size / 2 + iA)
        for i in range(iA, iB + 1):
            tup = tupleList[i]
            if i < mid: # top group
                tupleList[i] = (tup[0], tup[1], tup[2] + '0')
            else: # bottom group
                tupleList[i] = (tup[0], tup[1], tup[2] + '1')
        shannon_fano_encoder(iA, mid - 1)
        shannon_fano_encoder(mid, iB)

def byteWriter(bitStr, outputFile, k):
    global bitStream
    bitStream += bitStr
    while len(bitStream) > 8: # write byte(s) if there are more then 8 bits
        byteStr = bitStream[:8]
        bitStream = bitStream[8:]
        outputFile.write(chr(int(byteStr, 2)))

def shannon():

    if len(sys.argv) != 5 or sys.argv[4] < 2 or sys.argv[4] > 16 or not (sys.argv[1] == 'd' or sys.argv[1] == 'e'):
        print 'Usage: shannon.py [e|d] [path]InputFileName [path]OutputFileName [k number]'
        sys.exit()
    
    mode = sys.argv[1] # encoding/decoding
    inputFile = sys.argv[2]
    outputFile = sys.argv[3]
    k = int(sys.argv[4])

    #get the file size
    fileSize = os.path.getsize(inputFile)
    fi = open(inputFile, 'rb')
    byteArr = fi.read(fileSize)
    buffg = ""
    buffk = ""
    for x in byteArr:
    	byte = format(ord(x), 'b')
    	buffk += '0' * (8 - len(byte)) + byte
    buffg = [buffk[x:x+k] for x in range(0, len(buffk),k)]
    # for b in range(len(buffg)):
    #     buffg[b] = '0' * (k - len(buffg[b])) + buffg[b]
    byteArr = bytearray(byteArr)
    trash = ""
    if len(buffg[-1]) < k:
        trash = buffg[-1]
        del buffg[-1]
    fi.close()
    fileSize = len(byteArr)

    if mode == 'e':
        encoding()
    elif mode == 'd':
        decoding()

def encoding(): # FILE ENCODING

    #dict creation
    freqList = {}
    for b in buffg:
        if b in freqList.keys():
            freqList[b] += 1
        else:
            freqList[b] = 1
    tupleList = []
    for b in freqList.keys():
        if freqList[b] > 0:
            tupleList.append((freqList[b], b, ''))
    # sort the list according to the frequencies descending
    tupleList = sorted(tupleList, key=lambda tup: tup[0], reverse = True)
    shannon_fano_encoder(0, len(tupleList) - 1)

    maxTup2 = 0
    for tup in tupleList:
        if len(tup[2]) > maxTup2:
            maxTup2 = len(tup[2])

    dic = dict([(tup[1],tup[2] + (maxTup2 - len(tup[2])) * '0' ) for tup in tupleList])
    print dic
    print '\n'
    del tupleList # unneeded anymore

    #encoding below
    bitStream = ''
    fo = open(outputFile, 'wb')
    print len(dic)
    fo.write(chr(len(dic) - 1)) # first write the number of encoding tuples
    fo.write(chr(maxTup2 - 1)) # left dict key number

    #dictionary -> file
    for (byteValue, encodingBitStr) in dic.iteritems():
        bitStr = byteValue.encode()
        byteWriter(bitStr, fo, k)
        bitStr = bin(len(encodingBitStr) - 1) # 0b0 to 0b111
        bitStr = bitStr[2:]
        bitStr = '0' * (int(math.log(len(dic),2)) - len(bitStr)) + bitStr # add 0's if needed for 3 bits
        byteWriter(bitStr, fo, k)
        # encodingBitStr = '0' * (k -  len(encodingBitStr)) + encodingBitStr
        byteWriter(encodingBitStr, fo, k)

    bitStr = bin(fileSize - 1)
    bitStr = bitStr[2:] # remove 0b
    bitStr = '0' * (32 - len(bitStr)) + bitStr # add 0's if needed for 32 bits
    byteWriter(bitStr, fo, k)

    #text
    for b in buffg:
        byteWriter(dic[b], fo, k)

    #if we have any more leftovers
    byteWriter('0' * 8, fo, k) # to write the last remaining bits (if any)

    #for leftover trash
    if trash:
        fo.write(trash)
        fo.write(chr(len(trash)))
        print 'trash= ' + str(trash)
        print 'trashLength= ' + str(len(trash))
    else:
        fo.write(chr(0))
    fo.close()

def decoding(): # FILE DECODING

    #buffk is the main bitStream

    #count of different symbols
    bitPosition = 0
    n = int(buffk[:8], 2) + 1
    lenght = n
    buffk = buffk[8:]

    #get max left key length
    maxTupLength = int(buffk[:8], 2) + 1
    buffk = buffk[8:]

    #get trash length from the end of the file
    trashLength = int(buffk[-8:], 2)
    print 'trashLength= ' + str(trashLength)
    buffk = buffk[:-8]

    #then remove trash if any exists (also from the end of the file)
    trashOut = ''
    if trashLength > 0:
        for i in range (0, trashLength):
            trash = buffk[-8:]
            buffk = buffk[:-8]
            trashOut += chr(int(trash,2))

    trashOut = trashOut[::-1]
    print 'trashOut= ' + str(trashOut)

    #dictionary creation
    dic = dict()
    for i in range(n):

        #get dict key
        byteValue = buffk[:k]
        buffk = buffk[k:]

        #get index
        index = int(buffk[:int(math.log(lenght,2))], 2) + 1
        buffk = buffk[int(math.log(lenght,2)):]

        #get the second dict key
        encodingBitStr = buffk[:index]
        buffk = buffk[index:]

        # add to the dictionary
        dic[encodingBitStr] = byteValue 

    #dictionary finished
    print '\n'
    print dic

    #get fileSize
    numBytes = long(buffk[:32], 2) + 1
    buffk = buffk[32:]
    
    #start collecting the file output
    fileOutput = ''

    #check if we have any leftover zeros from encoding
    if len(buffk) % maxTupLength != 0:
        #if we do, delete them
        buffk = buffk[:-(len(buffk)%maxTupLength)]

    encodingBitStr = ''
    while buffk:

        #start collecting encoded data on maxTupLength
        encodingBitStr = buffk[:maxTupLength]
        buffk = buffk[maxTupLength:]

        #now iterate through our dictionary
        for (encoded, value) in dic.iteritems():
            #and find encoded value in our dictionary
            if encoded == encodingBitStr and len(encoded) == len(encodingBitStr):
                #if we do, then add it to fild output
                fileOutput += value

    #add leftovertrash which we couldn't encode
    fileOutput += trashOut

    fo = open(outputFile, 'w+')
    
    #write everything with bytes converted to chars
    while fileOutput:
        writing = fileOutput[:8]
        fileOutput = fileOutput[8:]
        fo.write(chr(int(writing,2)))
    fo.close()


shannon()
