#! /usr/bin/python

import subprocess

#function to decode the button pressed to a command
def case_eval(command):
    switcher = {
        "pause":"pause",
        "ff":"seek 10 0",
        "rw":"seek -10 0",
        "quit":"quit"
    }
    return switcher.get(command,"Invalid Command")


if __name__ == "__main__":

    usr_in = "cat"

    #reading user input 
    while( usr_in != "quit"):

        usr_in = raw_input("Enter a Command: \n")
        command = case_eval(usr_in)  
        
        #if the user command is valid send it to the fifo
        if(command != "Invalid Command"):
            cmd = "echo "+command+" > /tmp/mplayer-fifo"
            print subprocess.check_output(cmd, shell=True)
        else:
            print command
