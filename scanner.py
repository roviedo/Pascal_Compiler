import re
import sys
from constants import *

class Token:
    def __init__(self, token_name, value = None):
        self.name = token_name
        self.value = value
        
class Scanner:
    def __init__(self):
        self.data = ""
        self.tokens = []
        self.variable_matcher = re.compile('^([A-Za-z]|(_))([A-Za-z]|(_)|[0-9])*$')

    def read_file(self, testfile):
        #self.data  = open('variable_test.pas' , 'r').read()
        self.data = open(testfile, 'r').read()
        for symbol, token in symbols.items():
            if symbol != '.' and symbol != '=' and symbol != ':':
                self.data = self.data.replace(str(symbol), ' ' + symbol + ' ')
        #print "\nthis is before replace", self.data
        self.data = self.data.replace('end.' , 'end . ')
        self.data = self.data.split()
        
    def variable(self):
        #begin with letter or underscore
        #Can only contain letters, numbers, or underscore
        # Cannot contain blankspaces
        #elif ....
        pass
    def split_data(self):
        newdata = []
        for i in self.data:
            if i.endswith(";"):
                newdata.append(i[:-1])
                newdata.append(i[-1])
            elif i.endswith("."):
                newdata.append(i[:-1])
                newdata.append(i[-1])
            elif i.endswith(","):
                newdata.append(i[:-1])
                newdata.append(i[-1])
            elif i.endswith(":"):
                newdata.append(i[:-1])
                newdata.append(i[-1])
            else:
                newdata.append(i)
        self.data = newdata
        

    def tokenize_file(self):
        for i in self.data:
            if i in keywords:
                self.tokens.append(Token(keywords[i],i))
            elif i in operators:
                self.tokens.append(Token(operators[i]))
            elif i in symbols:
                self.tokens.append(Token(symbols[i]))
            elif i.isdigit():
                #print "TK_INTLIT"
                self.tokens.append(Token('TK_INTLIT', value = int(i)))
            elif self.isreal(i):
                #print "TK_REAL"
                self.tokens.append(Token('TK_REALLIT', value = float(i)))
            elif self.variable_matcher.match(i):
                #print "TK_IDENTIFIER"
                self.tokens.append(Token('TK_IDENTIFIER', value = i))
            else:
                print "Error", i
        
        #print self.tokens
        #for token in self.tokens:
         #   print token.name
        return self.tokens
    def isreal(self, i):
        try:
            result = str(float(i)) == i
            return result
        except ValueError:
            return False
