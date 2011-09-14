from constants import *

class Token:
    def __init__(self, token_name):
        self.name = token_name

class Scanner:
    def __init__(self):
        self.data = ""
        self.tokens = []
    def read_file(self):
        self.data  = open('test1.pas' , 'r').read().split()
        print self.data
    
    def tokenize_file(self):
        for i in self.data:
            if i in keywords:
                print "Got keyword" , keywords[i]
                self.tokens.append(Token(keywords[i]))
            elif i in operators:
                print "Got operators" , operators[i]
                self.tokens.append(Token(operators[i]))
            elif i in symbols:
                print "Got symbols" , symbols[i]
                self.tokens.append(Token(symbols[i]))
            else:
                print "Error", i
        
        print self.tokens
        for token in self.tokens:
            print token.name

def main():
    x = Scanner()
    x.read_file()
    x.tokenize_file()

if __name__ == "__main__":
    main()
