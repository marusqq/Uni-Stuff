    #!/usr/bin/python
    # -*- coding: UTF-8 -*-

    # Authors:
      # Marius Pozniakovas
      # Lukas Miežys

    # Special thanks to:
        # Aurimas Garnevičius - general help and ideas
        # Kipras Šivickas - logic of Hill cipher

    # Some of the tasks saved for the exam:
      # 1 - http://prntscr.com/piuu23 , http://prntscr.com/piuu4h
      # 2 - http://prntscr.com/piutrf
      # 3 - https://prnt.sc/piuu8u, http://prntscr.com/piuuek, http://prntscr.com/piuufx
      # 4 - http://prntscr.com/piuuk4, http://prntscr.com/piuumg
      # 5 - https://prnt.sc/piuvex
      # 5.1 - [[74, 74], [65, 73], [91, 69], [68, 73], [95, 73], [91, 65], [79, 83], [92, 65], [68, 73], [65, 73], [86, 75], [75, 75], [86, 86], [84, 83], [74, 82], [91, 90], [92, 69], [92, 74], [70, 75], [75, 69], [94, 82], [93, 73], [94, 80], [78, 77], [70, 84], [86, 83], [74, 84], [86, 82], [75, 85], [68, 79], [77, 73], [91, 79], [72, 65], [67, 69], [95, 73], [70, 76], [90, 65], [84, 83], [65, 73], [90, 85], [75, 73], [66, 65], [92, 65], [93, 73], [86, 86], [84, 83], [92, 65], [86, 86], [76, 82], [94, 84], [74, 84], [68, 79], [95, 79], [65, 65], [93, 79], [90, 73], [77, 80], [74, 73], [94, 84], [74, 75], [70, 76], [68, 79], [79, 85], [75, 83], [92, 65], [90, 75], [77, 82], [75, 65], [90, 65], [77, 80], [93, 73], [92, 73], [94, 84], [76, 83], [93, 75], [69, 85], [74, 68], [31, 115]]


      # 5.2 - [[223, 155], [220, 146], [194, 149], [217, 146], [202, 153], [198, 145], [195, 131], [193, 147], [217, 146], [220, 146], [203, 147], [222, 154], [214, 143], [208, 136], [198, 130], [223, 139], [197, 151], [201, 152], [219, 146], [210, 148], [210, 131], [200, 155], [210, 129], [223, 156], [198, 140], [210, 138], [194, 132], [210, 139], [195, 133], [221, 148], [216, 154], [202, 159], [213, 146], [210, 156], [202, 153], [223, 149], [199, 145], [208, 136], [220, 146], [210, 132], [222, 152], [215, 152], [193, 147], [200, 155], [214, 143], [208, 136], [193, 147], [214, 143], [192, 128], [214, 133], [194, 132], [221, 148], [206, 159], [212, 154], [204, 157], [207, 153], [193, 130], [223, 152], [214, 133], [223, 154], [223, 149], [221, 148], [199, 133], [199, 131], [193, 147], [207, 155], [193, 128], [214, 144], [199, 145], [193, 130], [200, 155], [201, 155], [214, 133], [192, 129], [200, 153], [197, 143], [211, 149], [149, 166]]


      # 5.3 [[81, 21], [81, 16], [89, 9], [73, 13], [77, 12], [73, 14], [78, 9], [67, 10], [74, 9], [67, 24], [95, 7], [93, 17], [77, 11], [89, 16], [85, 23], [79, 12], [73, 24], [76, 9], [78, 17], [67, 24], [90, 5], [91, 19], [89, 16], [77, 10], [77, 11], [74, 19], [71, 10], [91, 23], [93, 21], [70, 11], [85, 19], [67, 7], [65, 8], [66, 27], [74, 19], [71, 10], [77, 10], [73, 8], [92, 1], [74, 5], [83, 20], [67, 15], [94, 4], [66, 25], [83, 23], [68, 12], [71, 2], [75, 8], [78, 3], [83, 23], [68, 9], [74, 1], [74, 17], [78, 19], [66, 5], [75, 20], [71, 14], [91, 23], [85, 16], [78, 19], [86, 11], [74, 25], [79, 12], [77, 20], [66, 25], [69, 13], [94, 4], [67, 24], [74, 19], [75, 16], [79, 18], [75, 15], [87, 21], [73, 8], [77, 10], [65, 26], [67, 24], [83, 23], [64, 27], [82, 21], [83, 6], [89, 17]]

      # 6 - https://prnt.sc/piuvlh

      # 6.1 - [[83, 89], [77, 72], [65, 90], [91, 72], [84, 73], [84, 88], [68, 88], [72, 78], [82, 69], [91, 88], [70, 86], [86, 91], [91, 78], [64, 88], [92, 74], [64, 76], [73, 76], [66, 84], [74, 71], [92, 89], [83, 76], [82, 85], [65, 68], [84, 91], [80, 73], [86, 73], [82, 69], [73, 66], [73, 66], [72, 78], [93, 76], [83, 89], [83, 72], [73, 70], [65, 82], [68, 94], [66, 90], [73, 72], [69, 92], [76, 90], [72, 68], [90, 74], [86, 73], [94, 79], [82, 69], [67, 76], [73, 72], [66, 91], [76, 65], [64, 76], [92, 77], [76, 71], [73, 72], [70, 85], [84, 77], [76, 90], [77, 76], [83, 77], [66, 77], [65, 64], [71, 90], [90, 73], [70, 68], [64, 86], [74, 68], [83, 72]]

      # 6.2 - [[175, 35], [124, 250], [182, 59], [113, 246], [182, 48], [107, 254], [187, 43], [103, 241], [177, 53], [112, 227], [164, 61], [124, 227], [169, 39], [102, 229], [163, 34], [96, 226], [166, 41], [117, 247], [172, 57], [98, 229], [191, 40], [108, 234], [169, 56], [125, 253], [181, 53], [111, 253], [184, 55], [109, 235], [180, 36], [118, 249], [181, 35], [102, 237], [161, 61], [114, 232], [187, 52], [103, 249], [162, 58], [118, 230], [182, 45], [110, 249], [173, 52], [124, 234], [181, 49], [114, 244], [160, 42], [99, 250], [169, 35], [113, 233], [161, 43], [98, 253], [166, 39], [97, 226], [164, 44], [122, 245], [174, 59], [96, 231], [185, 40], [123, 245], [189, 49], [109, 253], [162, 36], [118, 231], [170, 55], [121, 226], [175, 37], [124, 250], [187, 46], [98, 246], [191, 40], [101, 255], [188, 36], [127, 232], [187, 59], [126, 254], [163, 54], [108, 234], [175, 48], [113, 244], [179, 53], [100, 254], [165, 36], [121, 237], [161, 49], [100, 250], [170, 37], [109, 241], [188, 32], [118, 251], [168, 49]]

      # 6.3 - [[180, 55], [127, 249], [170, 55], [119, 249], [176, 34], [115, 236], [180, 54], [121, 252], [185, 43], [114, 227], [180, 53], [103, 234], [173, 52], [108, 236], [167, 48], [116, 238], [170, 52], [105, 224], [167, 35], [122, 250], [190, 32], [124, 229], [169, 53], [110, 252], [188, 55], [127, 234], [175, 45], [102, 239], [173, 47], [97, 229], [168, 61], [108, 242], [186, 62], [112, 250], [160, 56], [103, 228], [182, 44], [108, 246], [170, 40], [115, 230], [170, 50], [113, 248], [177, 39], [104, 238], [170, 59], [127, 225], [160, 63], [101, 226], [171, 33], [109, 235], [166, 48], [126, 227], [163, 63], [98, 236], [160, 55], [108, 237], [161, 33], [101, 250], [183, 39], [102, 247], [165, 41], [104, 246], [187, 38], [120, 242], [183, 50], [115, 236]]


      # 6.4 - [[95, 68], [64, 68], [74, 74], [73, 87], [73, 68], [91, 75], [91, 70], [70, 86], [64, 82], [66, 82], [78, 74], [91, 86], [68, 75], [72, 80], [65, 66], [72, 71], [85, 84], [83, 95], [75, 82], [65, 91], [83, 65], [84, 52]]





    import ast
    import numpy as np
    from math import ceil
    import itertools

    #define a function to print or not to print, nice!
    def printBrute (message):

        #define some letters that can't be in the decrypted message
        badcombos = ['aaa', 'ąąą', 'bbb', 'ccc', 'ččč', 'ddd', 'eee', 'ęęę', 'ėėė', 'fff', 'ggg', 'hhh', 'iii', 'įįį', 'yyy', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'rrr', 'sss', 'ššš', 'ttt', 'uuu', 'ųųų', 'ūūū', 'vvv', 'zzz', 'žžž',
        'w', 'x', 'q',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
        'Ø', 'Æ', 'Ã', 'Ñ' ,'Ë', 'Õ', 'Ì', 'Ï']

        #define some letters that should be in the decrypted message#goodcombos = []

        #setup
        goodtoprint = True
        upper_message = message.upper()

        upper_message = clean_text(upper_message)

        for word in badcombos:
            if (upper_message.find(word.upper()) != -1):
                goodtoprint = False

        if not upper_message.isalpha():
            goodtoprint = False


        if goodtoprint:
            print(upper_message + '\n')
            printBrute.counter = printBrute.counter + 1

        if printBrute.counter == 10:
            printBrute.counter = input("Did you check all of the texts? Press enter to continue:..")
            print("\033[H\033[J")
            printBrute.counter = 0

    def clean_text(text):
      text = text.replace(' ', '')
      text = text.replace('\n', '')
      text = text.replace('\r', '')
      return text


    #How many times have we outputted
    printBrute.counter = 0
    # ______          _                 _   _
    #|  _  \        | |               | | (_)
    #| | | |___  ___| | __ _ _ __ __ _| |_ _  ___  _ __
    #| | | / _ \/ __| |/ _` | '__/ _` | __| |/ _ \| '_ \
    #| |/ /  __/ (__| | (_| | | | (_| | |_| | (_) | | | |
    #|___/ \___|\___|_|\__,_|_|  \__,_|\__|_|\___/|_| |_|
    #



    print ("\nMIF Decoder v5")

    print("use https://decodermif.mariuspozniakov.repl.run/ for best experience :)\n\n ")

    print('''Affine Caesar - enter AC
    [BRUTEFORCE] [Key] [Start_of_Text]\n''')
    print('''Skytale - enter S
    [BRUTEFORCE] [Key]\n''')
    print('''Transposition (Perstatu) - enter T
    [BRUTEFORCE] [Key(String)] [Key(Number)]\n''')
    print('''Rail Fence - enter R
    [BRUTEFORCE] [Key]\n''')
    print('''Fleissner - enter F
    [TODO]\n''')
    print('''Bifid (Delastelle) - enter B
    [TODO]\n''')
    print('''Enigma - enter E
    [BRUTEFORCE] [KEY/ROTATORS] [KEY/REFLECT/ROTATORS]\n''')
    print('''Vigenere - enter V
    [KEY_GUESS] [KEY]\n''')
    print('''Hill - enter H
    [KEY]\n''')
    print('''Feistel - enter FE
    [BRUTEFORCE] [ITERATION_F]\n''')
    print('''Registry (7 lecture) - enter RE
    [KEY?]\n''')
    print('''Hash function (9 lecture) - enter HA
    [DOESN'T WORK]\n''')
    print('''Backpack (10 lecture) - enter BACK
    [KEYS]\n''')
    print('''Feistel v2 - enter FE2
    [EBC] [CBC] [CFB] [CRT]\n\n''')


    cipher = input()

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
        print(text_to_decipher + '\n')

        #start collecting input
        temp_text = ""
        while True:
          temp=input()
          temp.encode(encoding='UTF-8')
          if temp == "":
            break
          else:
            temp_text = temp_text + temp


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
                        printBrute(brute)
                    else:
                        if brute[:len(keyword)] == keyword:
                            printBrute(brute)

                    #:3 means letters of the start
                    #print(brute)
                    #print(" ")



        ##End of BruteforceCaesar

        BruteforceCaesar(text_to_decipher, eq1, eq2, keyword)

    elif cipher == 'G' or cipher == 'g':
        print("Nice g")




        # _____            _        _
        #/  ___|          | |      | |
        #|\ `--.  ___ _   _| |_ __ _| | ___
        # `--. \/ __| | | | __/ _` | |/ _ \
        #/\__/ / (__| |_| | || (_| | |  __/
        #\____/ \___|\__, |\__\__,_|_|\___|
        #             __/ |
        #            |___/

    elif cipher == 'S' or cipher == 's':

        print("\033[H\033[J")

        finished=[]

        #get the text
        print("Enter the text to decrypt and press enter twice to confirm:")
        message = ""

        #start collecting input
        while True:
          temp=input()
          if temp == "":
            break
          else:
            message = message + temp

        #remove the spaces
        message = clean_text(message)

        turns=input("Enter the number of turns if known:\n")

        #hardcore the hell out of fucking scytale
        if turns == "":
          for a in range(1, len(message)):
            if len(message)%a == 0:
              for k in range(0,a):
                for i in range (0,ceil(len(message)/a)):
                  finished.insert(i+(k*(ceil(len(message)/a))),message[(i*a)+k])
              #print the message
              printBrute (''.join(finished) + '\n')
              finished = []

        #if we have the number of turns
        else:
          turns = int(turns)
          #turns=int(len(message)/turns)

          for k in range(0,turns):
            for i in range (0,ceil(len(message)/turns)):
              finished.insert(i+(k*(ceil(len(message)/turns))),message[(i*turns)+k])

          #print the decrypted text
          print (''.join(finished))





        # _____                                   _ _   _
        #|_   _|                                 (_) | (_)
        #  | |_ __ __ _ _ __  ___ _ __   ___  ___ _| |_ _  ___  _ __
        #  | | '__/ _` | '_ \/ __| '_ \ / _ \/ __| | __| |/ _ \| '_ \
        #  | | | | (_| | | | \__ \ |_) | (_) \__ \ | |_| | (_) | | | |
        #  \_/_|  \__,_|_| |_|___/ .__/ \___/|___/_|\__|_|\___/|_| |_|
        #                        | |
        #                        |_|

    elif cipher == 'T' or cipher == 't':

        print("\033[H\033[J")


        def decrypt(msg, key):

            bruteforce = 0

            msg = clean_text(msg)

            #if we have a text
            if not key.isdigit() and not key == "":
                # calculate the order we need to apply to it, sorted by ASCII acrrodingly
                order = [key.find(x) + 1  for x in sorted(key)]

                # analyze the string so that we can reverse the result to x in encryption
                chunks = [msg[int(k+x*len(msg)//len(key))] for k in range(len(msg)//len(key)) for x in range(len(key))]

                # removing all the symbols
                chunks = ''.join(chunks)

                # retrive how each row was picked
                chunks = [chunks[i:i+len(key)] for i in range(0, len(chunks), len(key))]

                x = map(lambda k: ''.join([c for (y,c) in sorted(zip(order, k))]), chunks)
                print(''.join(x))

            #if we have a number
            else:

                if key == "":
                    bruteforce = 1

                if bruteforce != 1:
                    # Our number that will help us calculate
                    # the shit out of this cipher
                    key = int(key)

                    # Do a list of all possible variations of a key
                    perm = list(itertools.permutations(range(0, key)))

                    #temp_array = perm[1]

                    # The number of "columns" in our transposition grid:
                    numOfColumns = ceil(len(msg) / key)

                    # Each string in plaintext represents a column in the grid.
                    plaintext = [''] * numOfColumns

                    col = 0
                    row = 0

                    for i in range(0, len(perm)):
                        temp_array = perm[i]
                        print(temp_array)
                        # Start decoding
                        for symbol in msg:

                            if col == key:
                                    col = 0
                                    row += 1

                            else:
                                plaintext[temp_array[col]] += symbol
                                col += 1 # point to next column

                                # If there are no more columns OR we're at a shaded box, go back to
                                # the first column and the next row.
                                #print(temp_array[col])
                                #print (numOfColumns)
                                #if (temp_array[col] == numOfColumns) or (temp_array[col] == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                                #		col = 0
                                #		row += 1

                        printBrute(''.join(plaintext))
                        plaintext = [''] * numOfColumns

                else:
                    for o in range (1, 8):
                        # Do a list of all possible variations of a key
                        perm = list(itertools.permutations(range(0, o)))

                        #temp_array = perm[1]

                        # The number of "columns" in our transposition grid:
                        numOfColumns = ceil(len(msg) / o)

                        # Each string in plaintext represents a column in the grid.
                        plaintext = [''] * numOfColumns

                        col = 0
                        row = 0

                        for i in range(0, len(perm)):
                            temp_array = perm[i]
                            print(temp_array)
                            # Start decoding
                            for symbol in msg:

                                if col == o:
                                        col = 0
                                        row += 1

                                else:
                                    plaintext[temp_array[col]] += symbol
                                    col += 1 # point to next column

                                    # If there are no more columns OR we're at a shaded box, go back to
                                    # the first column and the next row.
                                    #print(temp_array[col])
                                    #print (numOfColumns)
                                    #if (temp_array[col] == numOfColumns) or (temp_array[col] == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                                    #		col = 0
                                    #		row += 1

                            printBrute(''.join(plaintext))
                            plaintext = [''] * numOfColumns



        #get the text
        print("Enter the text to decrypt and press enter twice to confirm:\n")
        message = ""

        #start collecting input
        while True:
            temp=input()
            temp.encode(encoding='UTF-8')

            if temp == "":
                break
            else:
                message = message + temp

        #get the keyword
        keyword = input("\nYour key (Just press enter if you have none): \n")
        print("\n")
        keyword.encode(encoding='UTF-8')

        #decrypt
        decrypt(message, keyword)

    elif cipher == 'B' or cipher == 'b':
        print ("nice b")




        #______      _ _  ______
        #| ___ \    (_) | |  ___|
        #| |_/ /__ _ _| | | |_ ___ _ __   ___ ___
        #|    // _` | | | |  _/ _ \ '_ \ / __/ _ \
        #| |\ \ (_| | | | | ||  __/ | | | (_|  __/
        #\_| \_\__,_|_|_| \_| \___|_| |_|\___\___|
    elif cipher == 'R' or cipher == 'r':

        print("\033[H\033[J")

        #https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/
        # This function receives cipher-text
        # and key and returns the original
        # text after decryption
        def decryptRailFence(cipher, key):

                # create the matrix to cipher
                # plain text key = rows ,
                # length(text) = columns
                # filling the rail matrix to
                # distinguish filled spaces
                # from blank ones
                rail = [['\n' for i in range(len(cipher))]
                                            for j in range(key)]

                # to find the direction
                dir_down = None
                row, col = 0, 0

                # mark the places with '*'
                for i in range(len(cipher)):
                        if row == 0:
                                dir_down = True
                        if row == key - 1:
                                dir_down = False

                        # place the marker
                        rail[row][col] = '*'
                        col += 1

                        # find the next row
                        # using direction flag
                        if dir_down:
                                row += 1
                        else:
                                row -= 1

                # now we can construct the
                # fill the rail matrix
                index = 0
                for i in range(key):
                        for j in range(len(cipher)):
                                if ((rail[i][j] == '*') and
                                    (index < len(cipher))):
                                        rail[i][j] = cipher[index]
                                        index += 1

                # now read the matrix in
                # zig-zag manner to construct
                # the resultant text
                result = []
                row, col = 0, 0
                for i in range(len(cipher)):

                        # check the direction of flow
                        if row == 0:
                                dir_down = True
                        if row == key-1:
                                dir_down = False

                        # place the marker
                        if (rail[row][col] != '*'):
                                result.append(rail[row][col])
                                col += 1

                        # find the next row using
                        # direction flag
                        if dir_down:
                                row += 1
                        else:
                                row -= 1
                return("".join(result))


        #get the text
        print("Enter the text to decrypt and press enter twice to confirm:\n")
        message = ""
        message.encode(encoding='UTF-8')

        #start collecting input
        while True:
            temp=input()
            temp.encode(encoding='UTF-8')

            if temp == "":
                break
            else:
                message = message + temp

        message = clean_text(message)

        #get the key
        print ("\nEnter the key for the rail fence" +
        "\n(Just press enter if you have none):")

        key = input()

        if key != "":
            print('\n' + decryptRailFence(message, int(key)))
        else:
            for i in range (2, 30):
                print("key: " + str(i))
                print(decryptRailFence(message, int(i)))
                print('\n')




    #____  ____   _   __   __
    #|_   ||   _| (_) [  | [  |
    #  | |__| |   __   | |  | |
    #  |  __  |  [  |  | |  | |
    # _| |  | |_  | |  | |  | |
    #|____||____|[___][___][___]

    elif cipher == 'H' or cipher == 'h':

            #Default alphabet
        abc='AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ'
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
            abc = "ABCDEFGHIYJKLMNOPRSTUVZ"

        elif temp_abc != "":
            temp_abc.encode(encoding='UTF-8')
            abc = temp_abc
            #Default Text to decipher
        text_to_decipher = '''EEČŠM IOIŪĖ TŲŠAF FĮJMŠ CŠĘCŽ
    ZLNYĖ DRZAR EPMNG ĄTŲGČ EGGTJ
    JHVĄK AEDUG FFGEŲ GŪEŽV CRĖSĮ
    ŲTAŽM KUĮJŲ SOOMM ĄUYČŽ MDLIB
    ĮŲJZC ĄŽVNĘ ŪĖDĘZ YĘŲVĄ UGJŠŽ
    MNĘSN BŠZČP ŠPCHE LJEBĮ G'''

        text_to_decipher.encode(encoding='UTF-8')

        #Enter text_to_decipher
        print("Enter your text to decipher or keep the default: ")
        print(text_to_decipher + '\n')

        #start collecting input
        temp_text = ""
        while True:
          temp=input()
          temp.encode(encoding='UTF-8')
          if temp == "":
            break
          else:
            temp_text = temp_text + temp


        if temp_text != "":
            temp_text.encode(encoding='UTF-8')
            text_to_decipher = temp_text

        text_to_decipher = clean_text(text_to_decipher)

        mod = len(abc)

        print ("Enter your keys: (a, b, c, d) \n")
        k = [21, -22, -7, 15]
        temp_keys = input();
        if temp_keys != "":
          temp_keys = temp_keys.split (",")
          t_keys = []
          for i in temp_keys:
            t_keys.append(int(i))
          k = t_keys

        k22 = k[0]
        k12 = k[1] * -1
        k21 = k[2] * -1
        k11 = k[3]

        finalString = ""

        for x in range (0, len(text_to_decipher) - 1, 2):
          m1 = k11 * abc.find(text_to_decipher[x]) + k21 * abc.find(text_to_decipher[x + 1])
          m2 = k12 * abc.find(text_to_decipher[x]) + k22 * abc.find(text_to_decipher[x + 1])
          m1 = m1%mod
          m2 = m2%mod
          finalString = finalString + abc[m1] + abc[m2]
        printBrute(finalString)

    #_   _ _
    #| | | (_)
    #| | | |_  __ _  ___ _ __   ___ _ __ ___
    #| | | | |/ _` |/ _ \ '_ \ / _ \ '__/ _ \
    #\ \_/ / | (_| |  __/ | | |  __/ | |  __/
    # \___/|_|\__, |\___|_| |_|\___|_|  \___|
    #          __/ |
    #         |___/
    elif cipher == 'V' or cipher == 'v':

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

      #length of alphabet
      n=len(abc)

      def prepare(text):
        text=text.upper()
        textn=u''
        for a in text:
            if a in abc:
                textn+=a
        return textn

      def Vigenere(text,key): #Vigenere cipher
        textn=prepare(text)
        keyn=prepare(key)
        textc=u""
        keys=[]
        lk=len(keyn)
        for i in range(0,lk):
            keys.append(abc.index(keyn[i]))
        lt=len(textn)
        for i in range(0,lt):
            textc+=abc[(abc.index(textn[i])-keys[i%lk])%n]
        return textc

      #Default Text to decipher
      text_to_decipher = '''SŲCJI ŽCJFI ICLIŽ ĖŠĘRL KVŲMI EUFTĄ ŲFĖUG SNCCĮ AISKŠ ČKŽCG TEĄIJ VŲDEI FOYOT BĄFYG VYIDŪ  '''

      text_to_decipher.encode(encoding='UTF-8')

      #Enter text_to_decipher
      print("Enter your text to decipher or keep the default: ")
      print(text_to_decipher + '\n')

      #start collecting input
      temp_text = ""
      while True:
        temp=input()
        temp.encode(encoding='UTF-8')
        if temp == "":
          break
        else:
          temp_text = temp_text + temp

      if temp_text != "":
          temp_text.encode(encoding='UTF-8')
          text_to_decipher = temp_text

      text_to_decipher = clean_text(text_to_decipher)

      #Do we have a key?
      guess_cipher = 0
      key_cipher = input("Enter the FULL key if you have one, leave blank if not\n");

      if key_cipher == '':
        key_cipher = input("Enter the start of the key if you know it\n");
        guess_cipher = 1

      key_cipher = clean_text(key_cipher)

      if guess_cipher == 0:
        print(Vigenere(text_to_decipher, key_cipher))
      else:
        print("\033[H\033[J")
        for length in range(1, 4):
          perm = list(itertools.permutations(abc, length))
          for array in perm:
            temp_key = ''.join(array)
            temp_key = key_cipher + temp_key

            print('bruteforced key: ' + temp_key)
            answer = input('Press enter to search for a next key...\nType anything and press enter to see the decrypted text'+ '\n' )
            if answer != '':
              printBrute(Vigenere(text_to_decipher, temp_key) + '\n')


    # _____      _
    #|  ___|    (_)
    #| |__ _ __  _  __ _ _ __ ___   __ _
    #|  __| '_ \| |/ _` | '_ ` _ \ / _` |
    #| |__| | | | | (_| | | | | | | (_| |
    #\____/_| |_|_|\__, |_| |_| |_|\__,_|
    #               __/ |
    #              |___/

    elif cipher == 'E' or cipher == 'e':

      print("\033[H\033[J")

      #Are we using
      print("Choose between enigma/reflected enigma" + '\n')
      reflect = input('Enter enigma / reflect to choose:  ')
      if reflect == "reflect":
        reflect = 1
      else:
        reflect = 0
      print (reflect)

      print("\033[H\033[J")


      #Default alphabet
      abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
      text_to_decipher = "ITDDL VYOGV XZCEQ GZFFY AZITJ VVXPF OCJCZ OVDWI NJRLF OOSVS XULXA AVGST CESOK MKRYX LXDOJ ZCBMU VLJEW DOKWI ZOLUL PWUZH EBXDH VBUUF NKOTA RKQLD SDJFH SKYVG IOMEW SRQUM FUYYA MCRBN JJEGC DOXOY HJPTQ EMCBS OZDXM UFEJU OYVEP NUYLO JLCRZ MWBNH FXHUL FDOZZ SILHC HSATU INDHA PYDEX RAUYD DLJZF HZJHE NOQEA WEXBU LPYOT TSNCJ XLEAU XSTEE ZIGGQ SLGEM TLTCW FUJXZ MZIZZ YGFAH BXZDU TRJEP KSJPM GVHFJ SQOUO VGRVV KDNRX YVYKX TJYHI YHQRT UTZTJ BJZKG HLSJS WWKZP KYRCL GKWQK WKOMC ROFAC TGHVW CDFHA ELUJF LDPGX VHGRT CZM"

      text_to_decipher.encode(encoding='UTF-8')

      #Enter text_to_decipher
      print("Enter your text to decipher or keep the default: ")
      print(text_to_decipher + '\n')

      #start collecting input
      temp_text = ""
      while True:
        temp=input()
        temp.encode(encoding='UTF-8')
        if temp == "":
          break
        else:
          temp_text = temp_text + temp


      if temp_text != "":
          temp_text.encode(encoding='UTF-8')
          text_to_decipher = temp_text

      alphabet = abc
      lg = len(alphabet)

      def numerify(text):
          res = []
          for letter in text:
              num = alphabet.index(letter)
              res.append(num)
          return res

      def stringify(numbers):
          res = ''
          for number in numbers:
              letter = alphabet[number]
              res += letter
          return res

      def rot(m, a):
          return (a+m) % len(alphabet)

      def rsubst(rot, a):
          return rot.index(a)

      def deenigma(text, k1, k2, L1, L2):
        res = []

        lt = len(text)

        mapL1 = dict()

        # sudarome atvirkstini keitini
        for i in range(0, lg):
            mapL1[L1[i]] = i

        mapL2 = dict()

        # sudarome atvirkstini keitini
        for i in range(0, lg):
            mapL2[L2[i]] = i

        # rotoriai
        for i in range(0, lt):
            k = i
            m1 = k%lg
            m2 = ((k-m1)//lg) % lg

            m1 = m1+k1
            m2 = m2+k2

            a = abc.index(text[i])

            a = (a+m2) % lg
            a = mapL2[a]
            a = (a-m2) % lg
            a = (a+m1) % lg
            a = mapL1[a]
            a = (a-m1) % lg
            res.append(a)

        for i in range(0, lt):
            res[i] = abc[res[i]]

        return (''.join(res))


      def enigma(text, k1, k2, L1, L2):
        res = []
        lt = len(text)

        mapL1 = dict()

        # sudarome keitini
        for i in range(0, lg):
            mapL1[i] = L1[i]

        mapL2 = dict()

        # sudarome keitini
        for i in range(0, lg):
            mapL2[i] = L2[i]

        # rotoriai
        for i in range(0, lt):
            k = i
            m1 = k%lg
            m2 = ((k-m1)//lg) % lg

            m1 = m1+k1
            m2 = m2+k2

            a = abc.index(text[i])

            a = (a+m1) % lg
            a = mapL1[a]
            a = (a-m1) % lg
            a = (a+m2) % lg
            a = mapL2[a]
            a = (a-m2) % lg

            res.append(a)
        return (res)

      def deEnigma(key, L1, L2, ciphertext):
          cipherVals = numerify(ciphertext)
          messageVals = []
          m1 = key[0]
          m2 = key[1]
          rIdx = 0

          for cipherVal in cipherVals:
              val = cipherVal
              val = rot(m2, val)
              val = rsubst(L2, val)
              val = rot(-m2, val)
              val = rot(m1, val)
              val = rsubst(L1, val)
              val = rot(-m1, val)

              m1 += 1
              rIdx += 1
              if (rIdx % len(alphabet)) == 0:
                  m2 += 1

              messageVals.append(val)

          return stringify(messageVals)



      text = text_to_decipher

      text = clean_text(text)

      brute = 0

      key1 = input ('Input key1 (default 24) [Enter ''brute'' to bruteforce]:   ')
      key2 = input ('Input key2 (default 2): [Enter ''brute'' to bruteforce]:   ')


      if key1 == "":
        key1 = 24
      elif key1 == "brute":
        brute = 1
        brutekey = 'key1'

      if key2 == "":
        key2 = 2
      elif key2 == "brute":
        brute = 1
        brutekey = 'key2'

      print('\n')


      L1_rotator = input("Copy 1st rotator numbers with spaces: x, y, ..." + '\n')
      #list  = L1_rotator.split()
      if L1_rotator == "":
        L1_rotator = [10, 2, 21, 18, 23, 6, 16, 14, 8, 11, 1, 25, 15, 20, 0, 24, 17, 19, 22, 5, 4, 3, 9, 12, 13, 7]

      else:
        L1_rotator = L1_rotator.split (",")

      L2_rotator = input("Copy 2st rotator numbers with spaces: x, y, ..." + '\n')
      #list  = L2_rotator.split()

      if L2_rotator == "":
        L2_rotator = [10, 2, 11, 18, 8, 20, 19, 25, 23, 1, 15, 9, 14, 6, 24, 0, 17, 7, 22, 21, 4, 12, 5, 3, 16, 13]
      else:
        L2_rotator = L2_rotator.split (",")

      #reflection
      if reflect == 1:
        reflection = input("Enter reflection numbers with spaces: x, y, ..." + '\n')

        if reflection == "":
          reflection = [2, 4, 0, 6, 1, 11, 3, 8, 7, 13, 16, 5, 15, 9, 18, 12, 10, 19, 14, 17, 25, 22, 21, 24, 23, 20]
        else:
          reflection = reflection.split(",")


      # convert each element as integers
      L1_list = []
      for i in L1_rotator:
        L1_list.append(int(i))

      L2_list = []
      for i in L2_rotator:
        L2_list.append(int(i))

      if reflect == 1:
        reflection_list = []
        for i in reflection:
          reflection_list.append(int(i))

      print("\033[H\033[J")

      if brute == 1:
        key = input("If you know what your decoded text starts with enter the keyword here:\n")

        if brutekey == 'key1':
          for i in range(1, 50):
            brutetext = deEnigma([int(i), int(key2)],
            L1_list, L2_list, text)
            if brutetext[:len(key)] == key:
              print(brutetext + '\n')
        elif brutekey == 'key2':
          for i in range(1, 50):
            brutetext = deEnigma([int(key1), int(i)],
            L1_list, L2_list, text)
            if brutetext[:len(key)] == key:
              print(brutetext + '\n')

      else:
        if reflect != 1:
          print(deEnigma([int(key1), int(key2)],
          L1_list, L2_list, text))
        else:
          tmp = enigma(text, key1, key2, L1_list, L2_list)

          for i in range(0, len(tmp)):
            tmp[i] = abc[reflection_list[tmp[i]]]

          tmp_text = ''.join(tmp)

          print (deenigma(tmp_text, key1, key2, L1_list, L2_list))

    #______   _     _       _
    #|  ___| (_)   | |     | |
    #| |_ ___ _ ___| |_ ___| |
    #|  _/ _ \ / __| __/ _ \ |
    #| ||  __/ \__ \ ||  __/ |
    #\_| \___|_|___/\__\___|_|

    elif cipher == 'FE' or cipher == 'fe' or cipher == 'Fe' or cipher == 'Ef':

      print("\033[H\033[J")

      #clear = lambda : os.system('cls' if os.name=='nt' else 'clear')

      def iter(M,k,f):
        r=M[1]
        l=int(M[0])^eval(f)
        return [r,l]

      #Default alphabet
      abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
      m = [[223, 155], [220, 146], [194, 149], [217, 146], [202, 153], [198, 145], [195, 131], [193, 147], [217, 146], [220, 146], [203, 147], [222, 154], [214, 143], [208, 136], [198, 130], [223, 139], [197, 151], [201, 152], [219, 146], [210, 148], [210, 131], [200, 155], [210, 129], [223, 156], [198, 140], [210, 138], [194, 132], [210, 139], [195, 133], [221, 148], [216, 154], [202, 159], [213, 146], [210, 156], [202, 153], [223, 149], [199, 145], [208, 136], [220, 146], [210, 132], [222, 152], [215, 152], [193, 147], [200, 155], [214, 143], [208, 136], [193, 147], [214, 143], [192, 128], [214, 133], [194, 132], [221, 148], [206, 159], [212, 154], [204, 157], [207, 153], [193, 130], [223, 152], [214, 133], [223, 154], [223, 149], [221, 148], [199, 133], [199, 131], [193, 147], [207, 155], [193, 128], [214, 144], [199, 145], [193, 130], [200, 155], [201, 155], [214, 133], [192, 129], [200, 153], [197, 143], [211, 149], [149, 166]]
      #print (type(text_to_decipher))

      #Enter text_to_decipher
      print("Enter your text to decipher or keep the default: ")
      print(m)
      print('\n')

      #start collecting input
      temp_text = ""
      while True:
        temp=input()
        if temp == "":
          break
        else:
          temp_text = temp_text + temp

      if temp_text != "":
          m = ast.literal_eval(temp_text)
          #m = (map(int, m)
      #print (text_to_decipher)
      #print (type(text_to_decipher)
      iter_function = '(m|k)^((m//16)&k)'
      print("Enter your iteration function or keep the default:" + '\n' + iter_function + '\n')
      temp_iter_function = input();
      if temp_iter_function != "":
        iter_function = temp_iter_function
      iter_function = iter_function.replace('m', 'r')
      print ("Changed all letters to r besides k...\n")


      #entering keys
      print("Are there any keys that are not known?")
      brute = input("enter Y or N:  ");
      k = np.array([-1, 147])
      if brute == 'Y' or brute == 'y' or brute == 'yes' or brute == 'Yes':
        temp_key = input ("Enter your keys without [], divided by ',', use -1 for unknown keys\n").split(",")

        k = []
        for i in temp_key:
          k.append(int(i))

        length_of_keys = len(k)

        key_slots = []
        for i in range(0, length_of_keys):
          if k[i] == -1:
            key_slots.append(i)
        print("\033[H\033[J")
        print (k)
        print (length_of_keys)
        print (key_slots)
        #temp_keys = input("Enter the places for unknown keys: (start with 0, divide by ','):   ").split (",")

      else:

        print("Enter your keys without [], divided by ',' , or keep the default:")
        print(k)
        print('\n')

        temp_keys = input();
        if temp_keys != "":
          temp_keys = temp_keys.split (",")
          t_keys = []
          for i in temp_keys:
            t_keys.append(int(i))
          k = t_keys

      print("\nYou can also enter a keyword if you have one.")
      keyword = input("Leave blank if the keyword is unknown:        \n")
      text = []

      if brute == 'Y' or brute == 'y' or brute == 'yes' or brute == 'Yes':
        print("\nSometimes more than one correct output comes out. Do not worry, it is completely normal\n")
        # one key
        if length_of_keys == 1:
          if not 0 in key_slots:
            #not tested may not work
            for pair in m:
              ats1 = iter(pair,k[0], iter_function)
              text.append(chr(ats1[1]))
              text.append(chr(ats1[0]))
            text = ''.join(text)
            printBrute(text)
            text = []
          else:
            #not tested may not work
            for i in range (0, 256):
              for pair in m:
                ats1 = iter(pair, i, iter_function)
                text.append(chr(ats1[1]))
                text.append(chr(ats1[0]))
              text = ''.join(text)
              if keyword != "":
                  if text[:len(keyword)] == keyword:
                    printBrute(text)
              else:
                  printBrute(text)
              text = []

        #two keys
        elif length_of_keys == 2:
          if not 1 in key_slots:
            if not 0 in key_slots: # 1 no, 0 no
              for pair in m:
                ats1=iter(pair,k[1],iter_function)
                ats2=iter(ats1,k[0],iter_function)
                text.append(chr(ats2[1]))
                text.append(chr(ats2[0]))
              text = ''.join(text)
              if keyword != "":
                  if text[:len(keyword)] == keyword:
                    printBrute(text)
              else:
                  printBrute(text)
              text = []
            else: #1 no, 0 yes
              for x in range (0, 256):
                for pair in m:
                  ats1=iter(pair,k[1],iter_function)
                  ats2=iter(ats1,x,iter_function)
                  text.append(chr(ats2[1]))
                  text.append(chr(ats2[0]))
                text = ''.join(text)
                if keyword != "":
                    if text[:len(keyword)] == keyword:
                      printBrute(text)
                else:
                    printBrute(text)
                text = []
          else:
            if not 0 in key_slots: # 1 yes, 0 no
              for x in range (0, 256):
                for pair in m:
                  ats1=iter(pair,x,iter_function)
                  ats2=iter(ats1,k[0],iter_function)
                  text.append(chr(ats2[1]))
                  text.append(chr(ats2[0]))
                text = ''.join(text)
                if keyword != "":
                    if text[:len(keyword)] == keyword:
                      printBrute(text)
                else:
                    printBrute(text)
                text = []
            else: # 1 yes, 0 yes
              for y in range (0, 256):
                for x in range (0, 256):
                  for pair in m:
                    ats1=iter(pair,x,iter_function)
                    ats2=iter(ats1,y,iter_function)
                    text.append(chr(ats2[1]))
                    text.append(chr(ats2[0]))
                  text = ''.join(text)
                  if keyword != "":
                      if text[:len(keyword)] == keyword:
                        printBrute(text)
                  else:
                      printBrute(text)
                  text = []
        #elif length_of_keys > 2:
          #todo length_of_keys > 2
        #if text.isalpha():
        #print(text)

      #not brute
      else:
        length_of_keys = len(k)
        for pair in m:
          if length_of_keys == 1:
            ats1=iter(pair,k[0],iter_function)
            text.append(chr(ats1[1]))
            text.append(chr(ats1[0]))

          elif length_of_keys == 2:
            ats1=iter(pair,k[1],iter_function)
            ats2=iter(ats1,k[0],iter_function)
            text.append(chr(ats2[1]))
            text.append(chr(ats2[0]))

          elif length_of_keys == 3:
            ats1=iter(pair,k[2],iter_function)
            ats2=iter(ats1,k[1],iter_function)
            ats3=iter(ats2,k[0],iter_function)
            text.append(chr(ats3[1]))
            text.append(chr(ats3[0]))
        text = ''.join(text)
        if keyword != "":
            if text[:len(keyword)] == keyword:
              printBrute(text)
        else:
            printBrute(text)
        text = []


    elif cipher == 'FE2' or cipher == 'fe2':

        def iter(M, k, f):
            r=M[1]
            l=M[0]^eval(f)
            return [r,l]


        def feistel(M, K, f):
            res = []

            for m in M:
                for k in K:
                    m=iter(m,k,f)
                res.append(m[::-1])
            return res

        def de_feistel(M, K, f):
            return (feistel(M, K[::-1], f))

        def ord_to_str(M):
            return (''.join([chr(item) for sublist in M for item in sublist]))

        def xor(a_block, b_block):
            return ([ a_block[0] ^ b_block[0], a_block[1] ^ b_block[1] ])

        print('Currently the available decipher modes are: EBC, CBC, CFB, CRT')
        mode = input('Enter the mode you want to decipher now:...\n')
        if mode.upper() == 'EBC':
            print('EBC:...\n\n\n\n')

            #Default Text to decipher
            C1 = [[83, 89], [77, 72], [65, 90], [91, 72], [84, 73], [84, 88], [68, 88], [72, 78], [82, 69], [91, 88], [70, 86], [86, 91], [91, 78], [64, 88], [92, 74], [64, 76], [73, 76], [66, 84], [74, 71], [92, 89], [83, 76], [82, 85], [65, 68], [84, 91], [80, 73], [86, 73], [82, 69], [73, 66], [73, 66], [72, 78], [93, 76], [83, 89], [83, 72], [73, 70], [65, 82], [68, 94], [66, 90], [73, 72], [69, 92], [76, 90], [72, 68], [90, 74], [86, 73], [94, 79], [82, 69], [67, 76], [73, 72], [66, 91], [76, 65], [64, 76], [92, 77], [76, 71], [73, 72], [70, 85], [84, 77], [76, 90], [77, 76], [83, 77], [66, 77], [65, 64], [71, 90], [90, 73], [70, 68], [64, 86], [74, 68], [83, 72]]
            #print (type(text_to_decipher))

            #Enter text_to_decipher
            print("Enter your text to decipher or keep the default: ")
            print(C1)
            print('\n')

            #start collecting input
            temp_text = ""
            while True:
                temp=input()
                if temp == "":
                    break
                else:
                    temp_text = temp_text + temp

            if temp_text != "":
                C1 = ast.literal_eval(temp_text)
                #m = (map(int, m)
            #print (text_to_decipher)
            #print (type(text_to_decipher)
            iter_function = '(r&k)|((k%16)^r)'

            print("Enter your iteration function or keep the default:" + '\n' + iter_function + '\n')
            temp_iter_function = input();
            if temp_iter_function != "":
                iter_function = temp_iter_function
            iter_function = iter_function.replace('m', 'r')
            print ("Changed all letters to r besides k...\n")

            K1 = [8, 201, 105]
            print("Enter your keys without [], divided by ',' , or keep the default:")
            print(K1)
            print('\n')

            temp_keys = input();
            if temp_keys != "":
                temp_keys = temp_keys.split (",")
                t_keys = []
                for i in temp_keys:
                    t_keys.append(int(i))
                K1 = t_keys

            print(ord_to_str(de_feistel(C1, K1, iter_function)))


        elif mode.upper() == 'CBC':
            print('CBC:...\n\n\n\n')

            #Default Text to decipher
            C1 = [[175, 35], [124, 250], [182, 59], [113, 246], [182, 48], [107, 254], [187, 43], [103, 241], [177, 53], [112, 227], [164, 61], [124, 227], [169, 39], [102, 229], [163, 34], [96, 226], [166, 41], [117, 247], [172, 57], [98, 229], [191, 40], [108, 234], [169, 56], [125, 253], [181, 53], [111, 253], [184, 55], [109, 235], [180, 36], [118, 249], [181, 35], [102, 237], [161, 61], [114, 232], [187, 52], [103, 249], [162, 58], [118, 230], [182, 45], [110, 249], [173, 52], [124, 234], [181, 49], [114, 244], [160, 42], [99, 250], [169, 35], [113, 233], [161, 43], [98, 253], [166, 39], [97, 226], [164, 44], [122, 245], [174, 59], [96, 231], [185, 40], [123, 245], [189, 49], [109, 253], [162, 36], [118, 231], [170, 55], [121, 226], [175, 37], [124, 250], [187, 46], [98, 246], [191, 40], [101, 255], [188, 36], [127, 232], [187, 59], [126, 254], [163, 54], [108, 234], [175, 48], [113, 244], [179, 53], [100, 254], [165, 36], [121, 237], [161, 49], [100, 250], [170, 37], [109, 241], [188, 32], [118, 251], [168, 49]]
            #Enter text_to_decipher
            print("Enter your text to decipher or keep the default: ")
            print(C1)
            print('\n')

            M2 = [[]]

            #start collecting input
            temp_text = ""
            while True:
                temp=input()
                if temp == "":
                    break
                else:
                    temp_text = temp_text + temp

            if temp_text != "":
                C1 = ast.literal_eval(temp_text)
                #m = (map(int, m)
            #print (text_to_decipher)
            #print (type(text_to_decipher)
            iter_function = '(r&k)|((k%16)^r)'

            print("Enter your iteration function or keep the default:" + '\n' + iter_function + '\n')
            temp_iter_function = input();
            if temp_iter_function != "":
                iter_function = temp_iter_function
            iter_function = iter_function.replace('m', 'r')
            print ("Changed all letters to r besides k...\n")

            K1 = [8, 201, 105]
            print("Enter your keys without [], divided by ',' , or keep the default:")
            print(K1)
            print('\n')

            temp_keys = input();
            if temp_keys != "":
                temp_keys = temp_keys.split (",")
                t_keys = []
                for i in temp_keys:
                    t_keys.append(int(i))
                K1 = t_keys

            IV1 = [75, 149]
            print("Enter your VECTORS without [], divided by ',' , or keep the default:")
            print(IV1)
            print('\n')

            temp_keys = input();
            if temp_keys != "":
                temp_keys = temp_keys.split (",")
                t_keys = []
                for i in temp_keys:
                    t_keys.append(int(i))
                IV1 = t_keys

            for i in range(len(C1)):
                ci = C1[i]
                cid = de_feistel([ci], K1, iter_function)[0]
                mi = xor(cid, IV1)
                IV1 = ci
                M2.append(mi)

            print (ord_to_str(M2))
            print ('\n')

        elif mode.upper() == 'CFB':
            print('CFB:...\n\n\n\n')

            #Default Text to decipher
            C1 = [[180, 55], [127, 249], [170, 55], [119, 249], [176, 34], [115, 236], [180, 54], [121, 252], [185, 43], [114, 227], [180, 53], [103, 234], [173, 52], [108, 236], [167, 48], [116, 238], [170, 52], [105, 224], [167, 35], [122, 250], [190, 32], [124, 229], [169, 53], [110, 252], [188, 55], [127, 234], [175, 45], [102, 239], [173, 47], [97, 229], [168, 61], [108, 242], [186, 62], [112, 250], [160, 56], [103, 228], [182, 44], [108, 246], [170, 40], [115, 230], [170, 50], [113, 248], [177, 39], [104, 238], [170, 59], [127, 225], [160, 63], [101, 226], [171, 33], [109, 235], [166, 48], [126, 227], [163, 63], [98, 236], [160, 55], [108, 237], [161, 33], [101, 250], [183, 39], [102, 247], [165, 41], [104, 246], [187, 38], [120, 242], [183, 50], [115, 236]]
            #Enter text_to_decipher
            print("Enter your text to decipher or keep the default: ")
            print(C1)
            print('\n')

            M2 = [[]]

            #start collecting input
            temp_text = ""
            while True:
                temp=input()
                if temp == "":
                    break
                else:
                    temp_text = temp_text + temp

            if temp_text != "":
                C1 = ast.literal_eval(temp_text)
                #m = (map(int, m)
            #print (text_to_decipher)
            #print (type(text_to_decipher)
            iter_function = '(r&k)|((k%16)^r)'

            print("Enter your iteration function or keep the default:" + '\n' + iter_function + '\n')
            temp_iter_function = input();
            if temp_iter_function != "":
                iter_function = temp_iter_function
            iter_function = iter_function.replace('m', 'r')
            print ("Changed all letters to r besides k...\n")

            K1 = [8, 201, 105]
            print("Enter your keys without [], divided by ',' , or keep the default:")
            print(K1)
            print('\n')

            temp_keys = input();
            if temp_keys != "":
                temp_keys = temp_keys.split (",")
                t_keys = []
                for i in temp_keys:
                    t_keys.append(int(i))
                K1 = t_keys

            IV1 = [101, 236]
            print("Enter your VECTORS without [], divided by ',' , or keep the default:")
            print(IV1)
            print('\n')

            temp_keys = input();
            if temp_keys != "":
                temp_keys = temp_keys.split (",")
                t_keys = []
                for i in temp_keys:
                    t_keys.append(int(i))
                IV1 = t_keys

            for i in range(len(C1)):
                ci = C1[i]
                IV1s = feistel([IV1], K1, iter_function)[0]
                mi = xor(ci, IV1s)
                IV1 = ci
                M2.append(mi)

            print (ord_to_str(M2))
            print ('\n')

        elif mode.upper() == 'CRT':
            print('CRT:...\n\n\n\n')

            #Default Text to decipher
            C1 = [[95, 68], [64, 68], [74, 74], [73, 87], [73, 68], [91, 75], [91, 70], [70, 86], [64, 82], [66, 82], [78, 74], [91, 86], [68, 75], [72, 80], [65, 66], [72, 71], [85, 84], [83, 95], [75, 82], [65, 91], [83, 65], [84, 52]]
            #Enter text_to_decipher
            print("Enter your text to decipher or keep the default: ")
            print(C1)
            print('\n')

            M2 = [[]]

            #start collecting input
            temp_text = ""
            while True:
                temp=input()
                if temp == "":
                    break
                else:
                    temp_text = temp_text + temp

            if temp_text != "":
                C1 = ast.literal_eval(temp_text)
                #m = (map(int, m)
            #print (text_to_decipher)
            #print (type(text_to_decipher)
            iter_function = '(r&k)|((k%16)^r)'

            print("Enter your iteration function or keep the default:" + '\n' + iter_function + '\n')
            temp_iter_function = input();
            if temp_iter_function != "":
                iter_function = temp_iter_function
            iter_function = iter_function.replace('m', 'r')
            print ("Changed all letters to r besides k...\n")

            print("Creating a counter function turning all r to m")
            f_counter = iter_function.replace('r', 'm')

            K1 = [8, 201, 105]
            print("Enter your keys without [], divided by ',' , or keep the default:")
            print(K1)
            print('\n')

            temp_keys = input();
            if temp_keys != "":
                temp_keys = temp_keys.split (",")
                t_keys = []
                for i in temp_keys:
                    t_keys.append(int(i))
                K1 = t_keys

            def create_counter(m,k):
                T = eval(f_counter)
                return [T,T]

            for i in range(len(C1)):
                ci = C1[i]
                Ti = create_counter(i, K1[0])
                Tis = feistel([Ti], K1, iter_function)[0]
                mi = xor(ci, Tis)
                M2.append(mi)

            print (ord_to_str(M2))
            print('\n')

        else:
            print('No such mode is implemented. Please try again')

    elif cipher == 'RE' or cipher == 're' or cipher == 'Re':
        def stream(c,xp,n):  # the keystream generation, c-coefficients, xp - initial state, n - number of bits
            x=[0,0,0,0,0,0,0,0]
            for i in range(0,8):
                x[i]=xp[i]
            sr=''
            for i in range(0,n):
                bt=0
                sr+=str(x[0])
                for j in range(0,8):
                    bt+=c[j]*x[j]
                for j in range(1,8):
                    x[8-j]=x[7-j]
                x[0]=bt%2
            return sr

        #stream cipher
        def str_cipher(t,c,xp): # t - plaintext (ASCII decimal list), c-coefficients, xp - initial state
            cp=[]
            k=len(t)
            sr=stream(c,xp,8*k)
            for i in range (0,k):
                cp.append(t[i]^int(sr[8*i:8*i+8],2))
            return cp

        def xor(x, y):
            return '{1:0{0}b}'.format(len(x), int(x, 2) ^ int(y, 2))



        # How to use
        t = np.array([60, 246, 224, 115, 8, 143, 169, 135, 116, 78, 56, 99, 145, 237, 59, 182, 86, 179, 0, 15, 220, 13, 95, 108, 212, 87, 225, 189, 195, 194, 153, 62, 236, 232, 125, 12, 146, 161, 139, 107, 81, 42, 120, 153, 251, 61, 165, 82, 169, 18, 20, 211, 11, 67, 105, 209])


        #Enter text_to_decipher
        print("Enter your numbers to decipher or press enter to keep the default: ")
        print(t)
        print('\n')

        #start collecting input
        temp_text = ""
        while True:
          temp=input()
          if temp == "":
            break
          else:
            temp_text = temp_text + temp

        if temp_text != "":
            t = ast.literal_eval(temp_text)

        print ("Removing the first text number...\n")
        first = t[0]
        second = t[1]
        t = np.delete(t, 0)

        letters = 'MI'
        print("Enter letters that are given or press enter to keep the default: ")
        print (letters)
        temp_letters = input()

        if temp_letters != "":
            letters = temp_letters.upper()


        print ("Starting logic...\n")

        first_number_bin = np.binary_repr(first, width = 8)
        second_number_bin = np.binary_repr(second, width = 8)

        first_letter_bin = (" ".join(f"{ord(i):08b}" for i in letters[0]))
        second_letter_bin = (" ".join(f"{ord(i):08b}" for i in letters[1]))

        first_answer = xor(first_letter_bin, first_number_bin)
        second_answer = xor(second_number_bin, second_letter_bin)

        first_answer = first_answer + second_answer[0]

        new_number = first_answer[::-1]

        xp = []
        for i in range(0, len(new_number)-1):
            xp.append(int(new_number[i]))

        all_bin = list(itertools.product([0, 1], repeat=8))
        for c in all_bin:

            cp=str_cipher(t,c,xp)
            text = ""
            for r in cp:
                text+= chr(r)
            printBrute (letters[0] + text)

    elif cipher == 'HA' or cipher == 'ha' or cipher == 'Ha':
        print ('[HAHA] sorry, too hard for me to code\n')

    elif cipher == 'back' or cipher == 'Back' or cipher == 'BACK':
        
        print('Due to differences between python and sage math cell, this will be less automated.')
        print('Use this link: http://bit.ly/BackpackDecipher ');
        print('There will be instructions at the link');



    else:
        print ("Not a cipher abbrevation: " + cipher)
