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
        self.curr_inst_index = 0
    def execute(self):
        for a, b in self.codes:
            #print "ThIs IS THE REGISTERS: " , self.registers
            print "this is the stack " , self.stack , "\n"
            if a == opcodes['pushi']:
                self.stack.append(b)
            elif a == opcodes['push']:
                if b not in self.registers:
                    self.registers[b] = None
                else:
                    self.stack.append(self.registers[b])
                    #print "This is stack" , self.stack
                    #print "after pushing b", b
            elif a == opcodes['move']:
                continue
            elif a == opcodes['movei']:
                continue
            elif a == opcodes['mult']:
                 i = self.stack.pop()
                 j = self.stack.pop()
                 k = j * i
                 self.stack.append(k)
                 #print "this is multiplication" , k , "\n"
            elif a == opcodes['pop']:
                result =self.stack.pop()
                #print "this is result" , result 
                if b != None:
                    self.registers[b] = result
            elif a == opcodes['halt']:
                continue
            elif a == opcodes['print']:
                if type(b) == int:
                    print self.registers[b]
                elif type(b) == str:
                    print b
            elif a == opcodes['println']:
                print b + "\n"
            elif a == opcodes['div']:
                 i = self.stack.pop()
                 j = self.stack.pop()
                 k = j / i
                 self.stack.append(k)
                 #print "this is division" , k , "\n"

            elif a == opcodes['add']:
                 i = self.stack.pop()
                 j = self.stack.pop()
                 k = j + i
                 self.stack.append(k)
                 #print "this is add" , k 
            elif a == opcodes['sub']:
                 i = self.stack.pop()
                 j = self.stack.pop()
                 k = j - i
                 self.stack.append(k)
                 #print "this is sub", k
            elif a == opcodes['dup']:
                continue
            elif a == opcodes['exch']:
                continue
            elif a == opcodes['equ']:
                i = self.stack.pop()
                j = self.stack.pop()
                k = j == i
                self.stack.append(k)
            elif a == opcodes['neq']:
                i = self.stack.pop()
                j = self.stack.pop()
                k = j != i
                self.stack.append(k)
            elif a == opcodes['leq']:
                i = self.stack.pop()
                j = self.stack.pop()
                k = j <= i
                self.stack.append(k)
            elif a == opcodes['geq']:
                i = self.stack.pop()
                j = self.stack.pop()
                k = j >= i
                self.stack.append(k)
            elif a == opcodes['greater']:
                i = self.stack.pop()
                j = self.stack.pop()
                k = j > i
                self.stack.append(k)
            elif a == opcodes['less']:
                i = self.stack.pop()
                j = self.stack.pop()
                k = j < i
                self.stack.append(k)
            elif a == opcodes['jfalse']: 
                i = self.stack[len(self.stack)-1]
                if not i:
                    while self.codes[self.curr_inst_index][0] != opcodes['label']:
                        del self.codes[self.curr_inst_index]
            elif a == opcodes['jtrue']: 
                i = self.stack[len(self.stack)-1]
                if i:
                    while self.codes[self.curr_inst_index][0] != opcodes['label']:
                        del self.codes[self.curr_inst_index]
                            
            elif a == opcodes['jmp']:
                #slice = []
                print "this is codes" , self.codes
                l= self.codes[b:self.curr_inst_index+1:1]
                #for i in range(b, self.curr_inst_index):
                #    slice.append(self.codes[i])
                #print "this is slice before", l
                l.reverse()
                print "this is slice ", l
                for i in l:
                    #print "this is i 0 " , i
                    if i[0] == opcodes['jmp']:
                        alteredjmp = (opcodes['jmp'], i[1]+len(l))
                        #print " im in if jump state..."
                        self.codes.insert(self.curr_inst_index+1,alteredjmp)
                    else:
                        self.codes.insert(self.curr_inst_index+1,i)
                        
                print "Codes after insert" , self.codes
                raw_input()
            self.curr_inst_index += 1
