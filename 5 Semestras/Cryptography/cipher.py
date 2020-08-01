#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys


cipher = input('''Cipher code?
Affine Caesar - AC
Skytale - S
Transposition (Perstatu) - T
Rail Fence - R
Fleissner - F
Bifid (Delastelle) - B
''')

#  ____                            
#/  __ \                           
#| /  \/ __ _  ___  ___  __ _ _ __ 
#| |    / _` |/ _ \/ __|/ _` | '__|
#| \__/\ (_| |  __/\__ \ (_| | |   
#\____/\__,_|\___||___/\__,_|_|

if cipher == 'AC' or cipher == 'ac':
    
    print("\033[H\033[J")

    #Default alphabet
    abc='ABCDEFGHIYJKLMNOPRSTUVZ'
    abc.encode(encoding='UTF-8')
    
    #Enter alphabet
    print('''Enter your alphabet or: 
1 - AaĄąBbCcČčDdEeĘęĖėFfGgHhIiĮįYyJjKkLlMmNnOoPpRrSsŠšTtUuŲųŪūVvZzŽž
2 - AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ
Default - ''' + abc)
    temp_abc = input()
    print("\n")
    
    if temp_abc == "1":
        temp_abc.encode(encoding='UTF-8')
        abc = "AaĄąBbCcČčDdEeĘęĖėFfGgHhIiĮįYyJjKkLlMmNnOoPpRrSsŠšTtUuŲųŪūVvZzŽž"
    
    elif temp_abc == "2":
        temp_abc.encode(encoding='UTF-8')
        abc = "AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ"
        
    elif temp_abc != "":
        temp_abc.encode(encoding='UTF-8')
        abc = temp_abc
        

    
    #Default Text to decipher
    text_to_decipher = '''Įmūms uvmko ėiyfy myvči uorbm 
nmcyc čjvyg hyvlc čvylŪ gcjym 
čbgsv mhrir smouj yč '''
              
    text_to_decipher.encode(encoding='UTF-8')
    
    #Enter text_to_decipher
    print("Enter your text to decipher or keep the default: ")
    temp_text = input(text_to_decipher + "\n")
    
    if temp_text != "":
        temp_text.encode(encoding='UTF-8')
        text_to_decipher = temp_text
    
    #Your Keyword
    keyword = input("\nYour keyword (Just press enter if you have none): ")
    keyword.encode(encoding='UTF-8')
    
    #Length of alphabet
    length_abc=len(abc)
    
    #Have you calculated the numbers / keys?
    print ("\nEnter numbers / keys from equation from the keyword" + 
    "\n(Just press enter if you have none):")
    eq1 = input("Number 1: ")
    eq2 = input("Number 2: ")
    
    if eq1 == "":
        eq1 = 0
    if eq2 == "":
        eq2 = 0
    
    print("\033[H\033[J")
    
    
    #Caesar cipher
    def Caesar(text,k1,k2):
        
        t = ''
        t.encode(encoding='UTF-8')
        
        for r in text:
            if r in abc:
                t+=r
                
        c = ''
        c.encode(encoding='UTF-8')
        
        for r in t:
            m=(abc.index(r)*k1 + k2)%length_abc
            c+=abc[m]
        return c
    ## end of Caesar cipher
    
    
    #Bruteforce Caesar cipher
    def BruteforceCaesar(text, n1, n2, keyword):
        
        #setbruteforceCaesar start
        n1start = 0
        n2start = 0
        
        
        if n1 == 0: 
            n1 = length_abc
        else:
            n1start = n1
            
        if n2 == 0:
            n2 = length_abc
        else:
            n2start = n2
        for r in range(n1start, n1):
            for i in range(n2start, n2):
                
                brute = Caesar(text, r, i) 
                
                #maybe you have a keyword
                #uncomment this if you do
                if keyword == "":
                    print(brute)
                    print(" ")
                else:
                    if brute[:len(keyword)] == keyword:
                        print(brute)
                        print(" ")
                
                #:3 means letters of the start
                #print(brute)
                #print(" ")
            
            
            
    ##End of BruteforceCaesar
    
    BruteforceCaesar(text_to_decipher, eq1, eq2, keyword)
    
elif cipher == 'G':
    print("Nice")
        
        
        

