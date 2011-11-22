"""Virtual Machine"""
import sys
from scanner import *
from constants import *
from parser import *

class VirtualMachine():
    def __init__(self, codes):
        self.codes = codes
        self.stack = []
    def execute(self):
        for a, b in self.codes:
            if a == opcodes['push']:
                self.stack.append(b)
            elif a == opcodes['move']:
                continue
            elif a == opcodes['movei']:
                continue
            elif a == opcodes['mult']:
                 i = self.stack.pop()
                 j = self.stack.pop()
                 k = j * i
                 self.stack.append(k)
            elif a == opcodes['pop']:
                self.stack.pop()
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
            elif a == opcodes['add']:
                 i = self.stack.pop()
                 j = self.stack.pop()
                 k = j + i
                 self.stack.append(k)
            elif a == opcodes['sub']:
                 i = self.stack.pop()
                 j = self.stack.pop()
                 k = j - i
                 self.stack.append(k)
            elif a == opcodes['dup']:
                continue
            elif a == opcodes['exch']:
                continue
