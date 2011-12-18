"""Virtual Machine"""
import sys
from scanner import *
from constants import *
from parser import *

class VirtualMachine():
    def __init__(self, codes):
        self.codes = codes
        self.stack = []
        self.registers = {}
    def execute(self):
        for a, b in self.codes:
            print "ThIs IS THE REGISTERS: " , self.registers
            if a == opcodes['pushi']:
                self.stack.append(b)
            elif a == opcodes['push']:
                if b not in self.registers:
                    self.registers[b] = None
                else:
                    self.stack.append(self.registers[b])
                    print "This is stack" , self.stack
                    print "after pushing b", b
            elif a == opcodes['move']:
                continue
            elif a == opcodes['movei']:
                continue
            elif a == opcodes['mult']:
                 i = self.stack.pop()
                 j = self.stack.pop()
                 k = j * i
                 self.stack.append(k)
                 print "this is multiplication" , k , "\n"
            elif a == opcodes['pop']:
                result =self.stack.pop()
                print "this is result" , result 
                if b != None:
                    self.registers[b] = result
            elif a == opcodes['halt']:
                continue
            elif a == opcodes['print']:
                print b
            elif a == opcodes['println']:
                print b + "\n"
            elif a == opcodes['div']:
                 i = self.stack.pop()
                 j = self.stack.pop()
                 k = j / i
                 self.stack.append(k)
                 print "this is division" , k , "\n"

            elif a == opcodes['add']:
                 i = self.stack.pop()
                 j = self.stack.pop()
                 k = j + i
                 self.stack.append(k)
                 print "this is add" , k 
            elif a == opcodes['sub']:
                 i = self.stack.pop()
                 j = self.stack.pop()
                 k = j - i
                 self.stack.append(k)
                 print "this is sub", k
            elif a == opcodes['dup']:
                continue
            elif a == opcodes['exch']:
                continue
