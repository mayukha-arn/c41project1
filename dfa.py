#header 
print ("Project 1 for CS 341 \n Section number: H01 \n Semester: Fall 2026 \n Written by: Mayukha Ajeesh Ramsha Nath, 31678168 \n Instructor: Marvin Nakayama, marvin@njit.edu")

#function
def emailanalyzer784():

    # function to analyze email addresses
    pass

emailanalyzer784()
#notes:

#all input/output thru standard input/output
#need to create an output file with outputs - either txt or Microsoft Word
#all functions, subroutines, and classes should end in 784

#part 0 - header

#should first print: 
'''Project 1 for CS 341
Section number: the section number you are enrolled in
Semester: Fall 2026
Written by: your first and last name, your NJIT UCID
Instructor: Marvin Nakayama, marvin@njit.edu '''

#part 1 - instructions

'''Your program asks the user to enter an integer m ≥ 0 specifying the number
of input strings to be processed, and your program prints out the value of m. If
m = 0, the program terminates. If the user specified m ≥ 1, your program enters
a loop indexed by i = 1, 2, . . . , m'''

#part 2 - within loop

'''In the ith iteration of the loop, your program prompts the user, “Enter string i
of m”, where i is the iteration number and m is the total number of strings to
enter, and your program then reads in the string. You may assume that the user
will only enter a string over Σ. After reading in the string, your program prints
the current value of i and the string. Then your program processes the string on
your DFA in the following manner.'''

'''on each transition that your DFA takes when processing the input string,
your program must print out the state before taking the transition, the symbol
read on the transition, and the state after taking the transition. Even if your
DFA is in a trap state, your program must do this for each symbol in the
string until it reaches the end of the string.'''

'''
after finishing processing each entire input string, your program prints if the
string is accepted or rejected based on the state in which the DFA ended.
'''

#part 3 - end loop

'''after processing the mth string, your program terminates.'''





