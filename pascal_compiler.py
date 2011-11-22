#!usr/bin/env python

import sys
from parser import *
from scanner import *

def main():
    
    x = Scanner()
    x.read_file()
    print "finish reading file ..."
    tokens = x.tokenize_file()   
    print "finished tokenizing..."
    y = Parser(tokens)
    #y.print_tokens()
    #y.next_token()
    print "starting parser..."
    codes = y.parse()
    print codes
if __name__ == "__main__":
    main()
