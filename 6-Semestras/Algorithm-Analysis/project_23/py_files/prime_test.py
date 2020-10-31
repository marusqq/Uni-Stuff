#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com, marius.pozniakovas@mif.stud.vu.lt"
'''script for 23rd task of Algorithm Analysis'''

#for eratosthenes
from math import sqrt

#for miller_rabin
from random import randint
from math import pow

#for calculating time
from time import perf_counter
from datetime import datetime

def eratosthenes(check_if_prime):
    '''function that returns true/false if check_if_prime is a prime number
    uses eratosthenes sieve algorithm'''

    # Algorithm Idea:
    ## 1. Make a list of all numbers from 2 to x
    ## 2. Starting from 2, delete all multiples (except itself)
    ## 3. Repeat the step 2 (until square root of n)
    ## 4. Check if our number is still in list

    #1. get the list ready
    number_list = []
    for i in range(2, check_if_prime + 1, 1):
        number_list.append(i)

    #2 - 3. start from 2
    cycling_number = 2
        #until square root of n
    while cycling_number <= int(sqrt(check_if_prime)):
        #if we find a the number we are on right now in list
        if cycling_number in number_list:
            #cycle through the list and find multiples
            for divising_number in number_list:
                if int(divising_number) % int(cycling_number) == 0 \
                and divising_number > cycling_number:
                    number_list.remove(divising_number)
                    
        cycling_number = cycling_number + 1

    #after we finished
    if check_if_prime in number_list:
        return True
    else:
        return False

def miller_rabin(check_if_prime, iterations):
    '''function that returns true/false if check_if_prime is a prime number,
    uses miller_rabin algorithm'''

    #Algorithm Idea:
    ## 0. If the number is even we can return true instantly :), else:
    ## 1. Find n-1 = 2^k*m
    #### n = check_if_prime, n-1 = testing_number (before substraction), 
    #### m = testing_number
    ## 2. Choose random number: 1 < a < n-2
    ## 3. Compute b(0) = a^m(modn) and so on

    ### Example with 53 below.

    #0 (53 isnt even, move on) 
    if check_if_prime % 2 == 0:
        return False
    #1
    else:
        
        #get n-1 (53 - 1 = 52)
        testing_number = check_if_prime - 1

        #get lowest possible number that doesnt divide from 2 without reminder
        while (int(testing_number) % 2 == 0):
            testing_number = testing_number / 2

        #iterate and try to find
        while(iterations > 0):
            iterations = iterations - 1
            #if this test fails, the number is certainly not a prime number
            if single_miller_test(testing_number, check_if_prime) == False:
                return False
            
        #this number is possibly a prime number :)
        return True

def compute(random_num, divided_number, check_if_prime): 
    
    #suppose the answer is 1
    ans = 1

    #2 % 53 = 2
    random_num = random_num % check_if_prime
    
    #make sure its an int
    divided_number = int(divided_number)

    while (divided_number > 0):
        
        #if m is not even
        if (divided_number % 2 == 1):
            # 1) 1 * 2 % 53 = 2;
            # 3) 2 * 16 % 53 = 16; 
            ans = (ans * random_num) % check_if_prime

        # 1) 13 / 2 = 6; 
        # 2) 6 / 2 = 3;
        # 3) 3 / 2 = 1;
        divided_number = divided_number // 2

        # 1) 2 ^ 2 % 53 = 4 % 53 = 4; 
        # 2) 4 ^ 2 % 53 = 16
        # 3) 16 ^ 16 % 53 = 256 % 53 = 44
        random_num = pow(random_num, 2) % check_if_prime
    return ans

def single_miller_test(small_number, check_if_prime):
    '''miller test function
       if it returns true, that means check_if_prime is PROBABLY prime
       if it returns false, that means check_if_prime is NEVER prime'''

    #2, get random element (1 - 51, suppose we pick 2)
    rand = randint(1, check_if_prime - 2)

    ans = compute(rand, small_number, check_if_prime)

    if (ans == check_if_prime - 1 or ans == 1):
        return True
    
    while(small_number != check_if_prime - 1):
        ans = pow(ans, 2) % check_if_prime
        small_number = small_number * 2

        if ans == 1:
            return False
        
        elif ans == check_if_prime - 1:
            return True
        
    return False
    
def check_if_number_is_prime(check_if_prime = None, algorithm = '1', iterations_for_miller_rabin = 5, time = True):
    '''Checks if number is prime and then outputs the information on screen.
        Prime number checking may be done in two algorithms:
        [1 - Eratosthenes sieve, 2 - Miller-Rabin]
        send time = True, to see the time that algorithm was working'''

    if check_if_prime is None:
        #input
        check_if_prime = int(input('Enter a number to check: '))

    #start timer if time = True
    if time:
        #start timer
        start_of_algorithms = perf_counter()

    #if number is below 2, its a not prime number :)
    if check_if_prime < 2:
        prime = False

    #if number isnt below 2, lets use our algorithms
    else:
        if algorithm is None:
            algorithm = input('Choose algorithm:\n 1 - Eratosthenes sieve \n 2 - Miller-Rabin\n')
    
        #Eratosthenes sieve
        if str(algorithm) == '1':
            prime = eratosthenes(check_if_prime)

        #Miller-Rabin
        elif str(algorithm) == '2':
            prime = miller_rabin(check_if_prime, iterations_for_miller_rabin)
            
    if time:
        #finish timer
        time_passed = perf_counter() - start_of_algorithms

        if str(algorithm) == '1':
            print('Erasosthenes sieve algorithm was working for', round(time_passed, 2), 'seconds')
        elif str(algorithm) == '2':
            print('Miller-Rabin algorithm was working for', round(time_passed, 2), 'seconds')

    #print the result
    if prime:
        print('---', check_if_prime ,'is a PRIME number ---\n')
    else:
        print('---', check_if_prime ,'is NOT a prime number ---\n')
    
    return prime, time_passed