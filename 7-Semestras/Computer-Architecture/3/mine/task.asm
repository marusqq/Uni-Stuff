# Pirmoji programa 

.data
  name_surname:.string      "Marius Pozniakovas, 4 kursas, 1 grupė"
  space_char:  .string      " "
  newline:     .string      "\n"
  test_string: .string      "test"
  
  input_file:  .string      "input.csv"
  output_file: .string	    "output.csv"
  
  input_descriptor:  .word 0x0
  output_descriptor: .word 0x0
  
  .align 2
  buffer: .space 0x1000
  
.text

# Printing Author Details:
print_author_details:
   la a0, name_surname      # a0 <- name_surname
   li a7, 4	            # 4th system call -> PrintString
   ecall
  
   la a0, newline           # a0 <- newline
   li a7, 4                 # 4th system call -> PrintString
   ecall

main:

  # Setup file: INPUT.CSV
  li a7, 1024                  #set a7 to 1024 (open file)
  la a0, input_file            #set file name
  li a1, 0                     #set to READ mode
  ecall 
   
  la t1, input_descriptor      #get descriptor address
  sw a0, (t1)                  #save descriptor
  
  # Setup file: OUTPUT.CSV
  li a7, 1024                  #set a7 to 1024 (open file)
  la a0, output_file           #set file name
  li a1, 1                     #set to WRITE mode
  ecall 
  la t1, output_descriptor     #get descriptor address
  sw a0, (t1)  
  
  li a5, 0
  li a6, 100000

# Read the actual file char by char
start_line_read:
  li t2, 0                     # set starting Phase
                               # Default - 0
                               # 3 - not used
                               
  li t3, 1                     # 1 - writing line to output file, 0 - not writing line to output file
  addi a5, a5, 1
  
  lw a0, input_descriptor
  la a1, buffer
  call read_line
  
  # Chars we read
  #li a7, 1
  #ecall
  
  # Go back if to reading file
  beqz t3, start_line_read
 

  # Write to output file
  li a7, 64                    #set a7 to 64 (write)
  mv a2, a0                    #move file descriptor
  la a1, buffer		       #take buffer
  lw a0, output_descriptor     #output descriptor
  ecall
  
  ble a5, a6, start_line_read
  
  
  
  # Close Files
close_files:
  li   a7, 57                      # close file
  lw   a0, input_descriptor
  ecall
 
  li   a7, 57                      # close file
  lw   a0, output_descriptor
  ecall
  
  
  #exiting
  j exit
  
   
read_line:
   # a0 - descriptor
   # a1 - buffer address
   
   # Save registers used in stack
   addi sp, sp, -36
   sw s0, 0(sp)
   sw s1, 4(sp)
   sw s2, 8(sp)
   sw s3, 12(sp)
   sw s4, 16(sp)
   sw s5, 20(sp)
   sw s6, 24(sp)
   sw s7, 28(sp)
   sw ra, 32(sp)
   
   # Save a0 - a2:
   mv s0, a0
   mv s1, a1
   mv s2, a2
   
   li s4, 1            # How much we read
   
   li s11, 0           # Sign of number in line:
                          # 0 - Positive Sign
                          # 1 - Negative Sign
   li s10, 0           # One number count
   li a4, 0            # All line sum count
   li s8, 0            # Collecting number boolean
                          # True - when we are looking for the second digit of number
                          # False - when we found a number or are starting to look for one
   #li s9, 0            # Collecting Number
   
   read_line_loop:
   
      # Just skip if its the first line
      li t4, 1
      
      bne a5, t4, not_first_line
      li t3, 0
      
      # Not the first line
      not_first_line:
      
   
      
                    
      
      li a7, 63           # Set a7 to 63 (read mode)
      mv a0, s0           # Get descriptor
      mv a1, s1           # Get buffer
      li a2, 1            # Read 1 character
      ecall
      
      ble a0, x0, read_line_end # check for file ending
      lbu a0, (s1)
      
      
      
      
      # Now split the workflow into ->
         # 1. check for ;
         # 2. check for phase0
         # 3. check for phase1
         # 4. check for phase2
         
      #call print_buffer
 
      
           
                
                     
                          
                                    
      # Check if semicolon
      li t4, 59 # Ascii ; value
      beq a0, t4, semicolon
      
      # and if not - jump after the semicolon
      j after_semicolon

#                     _           _             
#                    (_)         | |            
#  ___  ___ _ __ ___  _  ___ ___ | | ___  _ __  
# / __|/ _ \ '_ ` _ \| |/ __/ _ \| |/ _ \| '_ \ 
# \__ \  __/ | | | | | | (_| (_) | | (_) | | | |
# |___/\___|_| |_| |_|_|\___\___/|_|\___/|_| |_|

      semicolon:
      
         # Two situations:
            # 1st or 2nd semicolon in line
               # Just add one
            # If 3rd and etc semicolons
               # Set to 0 when you find newline
            
            # Phases 0,1 < 2
            li t4, 2
            blt t2, t4, _0th_or_1st
            # Else:
            j _2nd_and_more
            
            
            _2nd_and_more:
               #li t4, 10 # Ascii for \n
               #bne a0, t4, after_phases
               #call print_buffer
               
               # Now for the hard part
               # We have 2 situations we may go to:
                  # If character is ; or \n -> SEMICOLON
                     # Add a number we found
                     # Jump to after_phases
                  # If character is else -> PHASE2
                     # number = number * 10 and number = number +/- digit
               #call print_buffer
               
               #found a semicolon
               # add digits to number
               add a4, a4, s10
               
               # set negative sign to 0
               li s11, 0
               
               # change collected number back to 0
               li s10, 0
               j after_phases

               
            _0th_or_1st:
               addi t2, t2, 1
               j after_phases

      after_semicolon:
      
      
      
      
      
      
      
      # Check if phase0
      beq t2, x0, phase0
      # and if not - jump after the phase
      j after_phase0
    
        
#        _                       ___  
#       | |                     / _ \ 
#  _ __ | |__   __ _ ___  ___  | | | |
# | '_ \| '_ \ / _` / __|/ _ \ | | | |
# | |_) | | | | (_| \__ \  __/ | |_| |
# | .__/|_| |_|\__,_|___/\___|  \___/ 
# | |                                 
# |_|                                 

      phase0:
        li t4, 88 # X in ascii
        beq a0, t4, bad_letter_skip
        li t4, 90 # Z in ascii
        beq a0, t4, bad_letter_skip
        j after_phases
        
        bad_letter_skip:
        li t3, 0
        after_bad_letter_skip:
        
        j after_phases
        
      after_phase0:
      
      
      
      
      
      
      
      
      # Check if phase1
      li t4, 1
      beq t2, t4, phase1
      # and if not - jump after the phase
      j after_phase1
      


#        _                      __ 
#       | |                    /_ |
#  _ __ | |__   __ _ ___  ___   | |
# | '_ \| '_ \ / _` / __|/ _ \  | |
# | |_) | | | | (_| \__ \  __/  | |
# | .__/|_| |_|\__,_|___/\___|  |_|
# | |                              
# |_|                              

      phase1:
      after_phase1:
      
      
      
      
      
      
      # Check if phase2
      li t4, 2
      beq t2, t4, phase2
      # and if not - jump after the phase
      j after_phase2
       
#        _                      ___  
#       | |                    |__ \ 
#  _ __ | |__   __ _ ___  ___     ) |
# | '_ \| '_ \ / _` / __|/ _ \   / / 
# | |_) | | | | (_| \__ \  __/  / /_ 
# | .__/|_| |_|\__,_|___/\___| |____|
# | |                                
# |_|     
                                 
      phase2:
      
         # First look for negative sign
         li t4, 45
         
         # If not negative skip this part
         bne a0, t4, skip_setting_negative_sign
         li s11, 1
         j after_phases
         
         skip_setting_negative_sign:
         
         
      	
      	      
         # Look for \n        
         li t4, 10 # Ascii for \n
         beq a0, t4, newline_found
         
         # If we didn't find it - skip it
         j after_check_added_sum   
         
         # If we found it, finish up the number
         newline_found:   
            add a4, a4, s10
            #call print_buffer
                        
            #---------------
            check_for_added_sum:
            #-------
            # Now check for every possible combination:
            # 15, 25, 35, 47, 101, 201
            
            # 15:
            li t4, 15
            beq a4, t4, after_check_added_sum
            
            # 25:
            li t4, 25
            beq a4, t4, after_check_added_sum
            
            # 35:
            li t4, 35
            beq a4, t4, after_check_added_sum
            
            # 47:
            li t4, 47
            beq a4, t4, after_check_added_sum
            
            # 101:
            li t4, 101
            beq a4, t4, after_check_added_sum
            
            # 201:
            li t4, 201
            beq a4, t4, after_check_added_sum
            
            #call print_buffer
            # if none of the numbers are right, just pass 0
            li t3, 0
                     
            j after_phases
         
         #-------
         after_check_added_sum:
         #---------------
         
         #---------------
         start_collecting_number:
         #-------
            # If the line is ruined already just skip this
            beqz t3, after_collecting_number
                  
            #number = number * 10
            li t4, 10
            mul s10, s10, t4
                  
            # Get int value of char stored
            addi t4, a0, -48
            
            # number = number +/- digit
            beqz s11, positive
            j negative
            
            # add if positive
            positive:
            add s10, s10, t4
            j after_phases
            
            # substract if negative
            negative:
            sub s10, s10, t4
            j after_phases
            
         #-------
         after_collecting_number:
         #---------------

      after_phase2:
      
      
      
      
      
      
      
      
      
      # After all phases logic continues the same
      after_phases:
         
         li t4, 10 # Ascii for \n
         beq a0, t4, read_line_end
      
         addi s1, s1, 1
         addi s4, s4, 1    
      
   
      j read_line_loop
   
      read_line_end:
         #call print_newline
         # Refix a1, s2.
         # a0 becomes result
         mv s9, a0
         mv a0, s4
         mv a1, s1
         mv a2, s2
      
      save_registers_input:   
         # Refix other registers
         lw s0, 0(sp)
         lw s1, 4(sp)
         lw s2, 8(sp)
         lw s3, 12(sp)
         lw s4, 16(sp)
         lw s5, 20(sp)
         lw s6, 24(sp)
         lw s7, 28(sp)
         lw ra, 32(sp)
   
         addi sp, sp, 36
         
         ble s9, x0, exit        
         
         ret

    
   
# Print buffer
print_buffer:

  save:
     # save a7
     mv t6, a0
     mv t5, a7
     mv t4, a1
     #mv t3, a3
     
  mv a0, a4
  li a7, 1
  ecall
  
  la a0, space_char
  li a7, 4
  ecall
  

  #li a7, 1
  #ecall
  
  #la a0, newline           # a0 <- newline
  #li a7, 4                 # 4th system call -> PrintString
  #ecall
  
  
  load_save:
     #get a0 and a7 back
     mv a0, t6
     mv a1, t4
     mv a7, t5
     
     
  ret 
  
print_newline:

  save_new_line:
     # save a7
     mv t6, a0
     mv t5, a7
     mv t4, a1
     #mv t3, a3
  
  mv a0, t3
  li a7, 1
  ecall
  
  la a0, newline           # a0 <- newline
  li a7, 4                 # 4th system call -> PrintString
  ecall
  
  load_save_newline:
     #get a0 and a7 back
     mv a0, t6
     mv a1, t4
     mv a7, t5
  ret 

#---------------------------------------------------------------
print_custom:

  save_custom_line:
     # save a7
     mv t6, a0
     mv t5, a7
     mv t4, a1
     #mv t3, a3
  
  la a0, test_string           # a0 <- newline
  li a7, 4                 # 4th system call -> PrintString
  ecall
  
  la a0, space_char
  li a7, 4
  ecall
  
  load_custom_newline:
     #get a0 and a7 back
     mv a0, t6
     mv a1, t4
     mv a7, t5
  ret 

#---------------------------------------------------------------
exit:
    li a7, 10   #  Exit 
    ecall
    

