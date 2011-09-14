from constants import *

class Token:
    def __init__(self, token_name, value = None):
        self.name = token_name
        self.value = value
class Scanner:
    def __init__(self):
        self.data = ""
        self.tokens = []
    def read_file(self):
        self.data  = open('test1.pas' , 'r').read().split()
        print self.data
        self.split_data()
    def split_data(self):
        newdata = []
        for i in self.data:
            if i.endswith(";"):
                newdata.append(i[:-1])
                newdata.append(i[-1])
            elif i.endswith(","):
                newdata.append(i[:-1])
                newdata.append(i[-1])
            else:
                newdata.append(i)
        self.data = newdata
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
            elif i.isdigit():
                self.tokens.append(Token('TK_INTLIT', value = int(i)))
            else:
                print "Error", i
        
        #print self.tokens
        for token in self.tokens:
            print token.name

def main():
    x = Scanner()
    x.read_file()
    x.tokenize_file()
    
if __name__ == "__main__":
    main()
