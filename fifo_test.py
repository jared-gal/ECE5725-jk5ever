#! /usr/bin/python

import subprocess


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

    while( usr_in != "quit"):

        usr_in = raw_input("Enter a Command: \n")
        command = case_eval(usr_in)  

        if(command != "Invalid Command"):
            cmd = "echo "+command+" > /tmp/mplayer-fifo"
            print subprocess.check_output(cmd, shell=True)
        else:
            print command
