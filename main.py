#!/usr/bin/python3

import subprocess

def helloWorld():
    subprocess.call("./hello")

# if this is not being imported as a module
if __name__ == "__main__":
    helloWorld()
