import xlsxwriter
import itertools
import os

# input -> string base 2
# output -> int base 10
def bin_to_dec(bin):
    
    bin = bin.replace(')', '')
    bin = bin.replace('(', '')
    bin = bin.replace(' ', '')
    bin = bin.replace(',', '')

    value = 0
    binary = []

    for bit in bin:
        binary.append(bit)
    
    #print(binary)
    
    for i in range(len(bin)):
        digit = binary.pop()
        if str(digit) == '1':
            value = value + pow(2, i)

    return value

# input -> int base 10
# output -> string base 2
def dec_to_bin(dec):
    res = format(dec, '06b')
    return res

def combinations(bits):
    return list(itertools.product([0, 1], repeat=bits))

def VLD():
    print('is k (', k ,') bigger than', bin_to_dec(byte_to_check), '?')
    if k > bin_to_dec(byte_to_check):
        finish_byte = '000001'
    else:
        finish_byte = '000000'
    
    zf = '0'
    baf = '0'

    return finish_byte+zf+baf

def NEG():

    #k - BYTE
    print('k - X = ans')
    print(k, bin_to_dec(byte_to_check), k - bin_to_dec(byte_to_check))
    answer = k - bin_to_dec(byte_to_check)

    if answer > 0:
        finish_byte = dec_to_bin(answer)
        print(finish_byte)
    else:
        finish_byte = '000000'
        baf = '1'
        if answer == 0:
            zf = '1'

    return finish_byte+zf+baf

def INC():
    #Z ← (X + 1) % k 
    print('incrementing this number', byte_to_check, bin_to_dec(byte_to_check))

    num = bin_to_dec(byte_to_check)
    
    if num >= k:
        baf = '1'
        finish_byte = '000000'

    else:
        num += 1
        if num >= k:
            num -= k
            if num == 0:
                zf = '1'
        finish_byte = dec_to_bin(num)

    if baf == '0':
        print('Incremented value:', bin_to_dec(finish_byte))
    else:
        print('wrong argument:', byte_to_check)

def DEC():
    #Z ← (k + X - 1) % k 
    print('decreasing this number', byte_to_check, bin_to_dec(byte_to_check))
    
    if bin_to_dec(byte_to_check) >= k:
        baf = '1'
        finish_byte = '000000'
        print('bad input!')

    else:
        ans = k + bin_to_dec(byte_to_check) - 1
        print('k + X - 1')
        print(k, bin_to_dec(byte_to_check), '-1', '=', ans)
        
        if ans >= k:
            ans -= k
            if ans == 0:
                zf = '1'
        finish_byte = dec_to_bin(ans)
        print('finish byte', finish_byte, bin_to_dec(finish_byte))

    return finish_byte+zf+baf

def CMPZ():
    finish_byte = '000000'
    if bin_to_dec(byte_to_check) == 0:
        zf = '1'
    return finish_byte+zf+baf

def OP3():
    
    power = 5
    print('x ^', power)
    num = bin_to_dec(byte_to_check)
    ans = pow(num, power)
    print(num, '^', power, ans)
    

    while ans >= k:
        ans -= k

    if ans == 0:
        zf = '1'

    print('finishing byte', dec_to_bin(ans))
    finish_byte = dec_to_bin(ans)

    return finish_byte+zf+baf

# #6 for answers, 1 for sf, 1 for baf
# byte_with_answers = '101000'
# byte_to_print = "".join(str(byte_with_answers))

# decimal = bin_to_dec(byte_with_answers)
# binary = dec_to_bin(decimal)
try:
    os.remove('excel.xlsx')
    print('file excel.xlsx removed')
except:
    print('file excel.xlsx was not removed')

workbook = xlsxwriter.Workbook('excel.xlsx')
worksheet = workbook.add_worksheet()

input_combinations = combinations(6)
row = 0
k = 38
debug = False

for byte_num in range(0, len(input_combinations)):
    
    byte_to_check = str(input_combinations[byte_num])
    zf = '0'
    baf = '0'
    
    print('current byte', byte_to_check)
    
    #do something here with the byte
    #---------------------------------
    #SHL
    byte_to_check = dec_to_bin(bin_to_dec(byte_to_check))

    one_bits = byte_to_check.count('0')

    finish_byte = dec_to_bin(one_bits)
    
    
    print(finish_byte)

    if finish_byte == '000000':
        zf = '1'


    
    #---------------------------------
    #slight pause
    if debug:
        input()

    #finish with result byte
    
    #dont forget sf, baf
    finish_byte = finish_byte + str(zf) + str(baf)
    for i in range(0, len(finish_byte)):
        worksheet.write(row, i, finish_byte[i])

    row += 1

workbook.close()
print('done!')