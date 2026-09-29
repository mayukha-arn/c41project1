output_file = "output.txt"
from email.mime import text


log784 = [] #lines on screen shown for output file
accepting_states = {8,9,10} #stores q8, q9, q10 as accepting states
trap_state = 11 #stores q11 as trap state

header784 = ("Project 1 for CS 341 \n Section number: H01 \n Semester: Fall 2026 \n Written by: Mayukha Ajeesh Ramsha Nath, 31678168 \n Instructor: Marvin Nakayama, marvin@njit.edu")

print(header784)
log784.append(header784)

#print to screen and remember output lines for output file
def output784(text):
    log784.append(text)
    print(text)

#log prompt and typed answer
def input784(prompt):
    text = input(prompt)
    log784.append(text)
    return text

#should only hold lowercase alphabetic characters
def letters784(ch):
    return ch.isalpha() and ch.islower()

#an edge not in diagram should go to trap state (q11)

def transition784(state,ch):
    #start state! - (q1)
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
    #trap state - (q11)
    return trap_state

def process_string784(string_input):
    state = 1
    for ch in string_input:
        next_state = transition784(state,ch)
        output784(f"Current state: {state}, Symbol read: {ch}, Next state: {next_state}")
        state = next_state
    return state in accepting_states

#read input from user
def read784():
    promptuser = input("Enter an integer m greater than 0 specifying the number of input strings to be processed: ")
    while True:
        text=input784(promptuser)
        try:
            m = int(text)
            if m >= 0:
                return m
        except ValueError:
            pass
        output784("Invalid input. Please enter an integer m greater than 0.")

#function to analyze email strings
def emailanalyzer784():
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

        output784("Program terminated - processing complete.")

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