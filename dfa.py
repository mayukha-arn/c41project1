#output_file = "output.txt"
log784 = []
accepting_states = {8,9,10}
trap_state = 11

header784 = "Project 1 for CS 341 \n Section number: H01 \n Semester: Fall 2026 \n Written by: Mayukha Ajeesh Ramsha Nath, 31678168 \n Instructor: Marvin Nakayama,"
#print ("Project 1 for CS 341 \n Section number: H01 \n Semester: Fall 2026 \n Written by: Mayukha Ajeesh Ramsha Nath, 31678168 \n Instructor: Marvin Nakayama, marvin@njit.edu")
log784.append(header784)

def output784(text):
    log784.append(text)
    print(text)

def input784(prompt):
    text = input(prompt)
    log784.append(text)
    return text

def letters784(ch):
    return ch.isalpha()

def transition784(state,ch):
    if state ==1:
        return 2 if letters784(ch) else trap_state
    if state == 2:
        if letters784(ch):
            return 2
        elif ch == ".":
            return 3
        elif ch == "@":
            return 4
        return trap_state
    if state == 3:
        return 2 if letters784(ch) else trap_state
    if state == 4:
        return 5 if letters784(ch) else trap_state
    if state == 5:
        if letters784(ch):
            return 5
        elif ch == ".":
            return 6
        return trap_state
    if state == 6:
        if ch == "c":
            return 7
        elif letters784(ch):
            return 5
        return trap_state
    if state == 7:
        if ch == "o":
            return 8
        elif ch == "m":
            return 9
        elif letters784(ch):
            return 5
        elif ch == ".":
            return 6
        return trap_state
    if state == 8:
        if ch == "m":
            return 10
        elif letters784(ch):
            return 5
        elif ch == ".":
            return 6
        return trap_state
    if state == (9,10):
        if letters784(ch):
            return 5
        elif ch == ".":
            return 6
        return trap_state
    return trap_state

def process_string784(string_input):
    state = 1
    for ch in string_input:
        next_state = transition784(state,ch)
        output784(f"Current state: {state}, Symbol read: {ch}, Next state: {next_state}")
        state = next_state
    accepted = state in accepting_states
    return accepted

#read input from user
def read784():
    text = input("Enter an integer m ≥ 0 specifying the number of input strings to be processed: ")
m = int(text)

if m == 0:
    print("Program terminated.")
else:
    print("Value of m:", m)
    for i in range(1, m + 1):
        string_input = input(f"Enter string {i} of {m}: ")
        print(f"Current value of i: {i}, String: {string_input}")
        
        print("Processing the string on the DFA...")
        
        if accepted:
            print("The string is accepted.")
        else:
            print("The string is rejected.")

#function
def emailanalyzer784():

    # function to analyze email addresses
    m = read784()
    output784(f"Value of m: {m}")
    if m == 0:
        output784("Program terminated.")
        return
    for i in range(1, m + 1):
        string_input = input784(f"Enter string {i} of {m}: ")
        output784(f"Current value of i: {i}, String: {string_input}")
        
        output784("Processing the string on the DFA...")
        
        accepted = process_string784(string_input)
        
        if accepted:
            output784("The string is accepted.")
        else:
            output784("The string is rejected.")
        output784("\n")  

def main784():
    emailanalyzer784()
    with open("output.txt", "w") as f:
        for line in log784:
            f.write(line + "\n")


main784()

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





