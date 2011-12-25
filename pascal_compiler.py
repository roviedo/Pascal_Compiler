#!usr/bin/env python

import sys
from parser import *
from scanner import *
from vm import *
def main():
    if len(sys.argv) < 2:
        print "Please follow program running scheme of python pascal_compiler.py testfile"
        exit(0)
    testfile = sys.argv[1]
    x = Scanner()
    x.read_file(testfile)
    print "finish reading file ..."
    tokens = x.tokenize_file()   
    print "finished tokenizing..."
    y = Parser(tokens)
    #y.print_tokens()
    #y.next_token()
    print "starting parser..."
    codes = y.parse()
    #print codes
    z = VirtualMachine(codes)
    b = z.execute()
if __name__ == "__main__":
    main()
