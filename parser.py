"""Parser"""
import sys
from scanner import *
from constants import *

class Parser():
    def __init__(self, tokens):
        """
        sets tokens returned from the tokenizer to tokens, it reverses them so that when we pop ,
        we pop whats in the beggining of the tokens. Previous_token is empty and current_token is set
        to the popped item from tokens.
        """
        self.tokens = tokens
        self.tokens.reverse()
        self.previous_token = None
        self.current_token = self.tokens.pop()
        self.codes = []
        self.symboltable = []
    def print_tokens(self):
        for i in self.tokens:
            print i.name

    def match(self, name, do_not_exit =False):
        """
        Checks if the current_token is equal to name and if it is
        it calls the function next_token.
        """
        
        if(self.current_token.name == name):
            print "MATCH: successfully matched" , self.current_token.name
            self.next_token()
            
            return True
        elif not do_not_exit:
            print "MATCH: error, was expecting: " + name + " got : " + self.current_token.name
            exit(0)
        return False
    def next_token(self):
        """
        Checks if tokens are greater than zero and sets previous_token to the current_token and current_token
        to the next item on the list
        """
        if len(self.tokens) > 0:
            self.previous_token = self.current_token
            self.current_token = self.tokens.pop()
        
            
    def parse(self):
        self.program_statement()
        #self.var_statement()
        self.declarations()
        self.begin_statement()
        print "finished begin statement"
        self.match(symbols['.'])
        print "finished match ."
        return self.codes
    def program_statement(self):
        """
        This function makes sure that program starts correctly
        Example: program name;
        """
        self.match(keywords['program'])
        self.match('TK_IDENTIFIER')
        self.match(symbols[';'])
        #print "Matched Program Statement successfully"

    def var_statement(self):
        self.match(keywords['var'])
        #self.match(keywords['TK_IDENTIFIER'])
        while(self.match('TK_IDENTIFIER')):
            self.symboltable.append(self.previous_token.value)
            self.codes.append((opcodes['push'] , self.symboltable.index(self.previous_token.value)))
            if self.match(symbols[','], do_not_exit =True):
                #print "reached a comma"
                continue
            elif self.match(symbols[':']):
                #print "got to colon"  
                break
    
        if self.match(keywords['integer'], do_not_exit = True):
            print "This var is an integer"
        elif self.match(keywords['string'], do_not_exit = True):
            print "This var is a string"
        elif self.match(keywords['boolean'], do_not_exit = True):
            print "this is a boolean"
        elif self.match(keywords['real']):
            print "This is a real"
    
    def prod_E(self):
        self.prod_T()
        self.prod_E_prime()
    def prod_E_prime(self):
        if self.match(operators['+'], do_not_exit = True):
            self.prod_T()
            self.codes.append((opcodes['add'], None)) 
            #print " got plus sign\n"
            self.prod_E_prime()
        elif self.match(operators['-'], do_not_exit = True):
            self.prod_T()
            self.codes.append((opcodes['sub'], None))
            #print"got minus sign\n"
            self.prod_E_prime()
        

        
    
    def prod_T(self):
        self.prod_F()
        self.prod_T_prime()
    def prod_T_prime(self):
        if self.match(operators['*'], do_not_exit = True):
            self.prod_F()
            self.codes.append((opcodes['mult'] , None))
            #print "got mult sign\n"
            self.prod_T_prime()
        elif self.match(operators['/'], do_not_exit = True):
            self.prod_F()
            self.codes.append((opcodes['div'] , None))
            #print "got div sign\n"
            self.prod_T_prime()
        elif self.match(operators['and'], do_not_exit = True):
            self.prod_F()
            #print "got boolean and\n"
            self.prod_T_prime()
        elif self.match(operators['shl'], do_not_exit = True):
            self.prod_F()
            #print "got shift left\n"
            self.prod_T_prime()
        elif self.match(operators['shr'], do_not_exit = True):
            self.prod_F()
            #print "got shift right\r"
            self.prod_T_prime()

    def prod_F(self):
        if self.match('TK_IDENTIFIER', do_not_exit = True):
            print "Got Identifier ...."
            
            lhs = self.previous_token
            if self.previous_token.value not in self.symboltable:
                print "UNDECLARED VARIABLE"
                exit(0)
            if self.match(operators[':='], do_not_exit = True):    
                self.assignment(lhs)
            else:
                print "Previous token: " , self.previous_token.name, "value", self.previous_token.value
                print "Current token: " , self.current_token.name, "value", self.current_token.value
                self.codes.append((opcodes['push'], self.symboltable.index(self.previous_token.value)))
                
        elif self.match('TK_INTLIT', do_not_exit = True):
            #print "Got Intlit"
            self.codes.append((opcodes['pushi'] , self.previous_token.value))
            return type(self.previous_token.value)
        elif self.match('TK_REALLIT' , do_not_exit = True):
            self.codes.append((opcodes['pushi'], self.previous_token.value))
            return type(self.previous_token.value)
        #elif self.match(symbols['(']):
        #    print "reached left parenthesis"
        #    self.prod_L()
        #    self.match(symbols[')'])
        #elif self.match(symbols[')']):
        #    print "reached right parenthesis"
        elif self.match(keywords['write'],do_not_exit =True):
            result = self.write_statement()
            self.codes.append((opcodes['print'], result))
        elif self.match(keywords['writeln'], do_not_exit = True):
            result = self.write_statement()
            self.codes.append((opcodes['println'], result))
        elif self.match(operators['-'], do_not_exit = True):
            self.prod_F()
            #print "Got minus sign in prod_F\n"
        
        else:
            print self.current_token.name
            print "Reached epsilon"
    def prod_L(self):
        self.prod_E()
        self.prod_L_prime()
    def prod_L_prime(self):
        if self.match(operators['='], do_not_exit = True):
            self.prod_E()
        elif self.match(operators['<>'], do_not_exit = True):
            self.prod_E()
        elif self.match(operators['>'], do_not_exit = True):
            self.prod_E()
        elif self.match(operators['<'], do_not_exit = True):
            self.prod_E()
        elif self.match(operators['<='], do_not_exit = True):
            print "matched less than or equal to\n"
            self.prod_E()
        elif self.match(operators['>='], do_not_exit = True):
            self.prod_E()
        elif self.match(operators['in'], do_not_exit = True):
            self.prod_E()
    
    def declarations(self):
        if self.current_token.name == keywords['var']:
            self.var_statement()
            self.match(symbols[';'])
            self.declaration_tail()

    def declaration_tail(self):
        self.declarations()

    def begin_statement(self):
        """
        FOR NEXT TIME HAVE TO FINISH BEGIN_STATEMENT  IF CLAUSE TO CONTINUE CORRECTLY
        """
        self.match(keywords['begin'])
        print "successfully matched first begin\n"
        if self.tokens and self.current_token.name != keywords['end']:
            #print "matched end\n"
            self.statement_list()
        
        self.match(keywords['end'])
        #print "successfully matched first end\n"
    
    def write_statement(self):
        self.match(symbols['('])
        self.match(symbols['"'])
        result = ''
        while self.current_token.name != symbols['"']:
            print "this is value" , self.current_token.value
            print "this is name" , self.current_token.name
            result += self.current_token.value + ' '
            self.next_token()
        self.match(symbols['"'])
        self.match(symbols[')'])
        return result

    def statement_list(self):
        """
        while there's tokens left and keyword is not end do statement() function
        """
        while self.tokens and self.current_token.name != keywords['end']:        
            self.statement()
            #self.match(symbols[';'])
            #print "successfully matched semicolon\n"
            
             

    def statement(self):
        if self.current_token.name == keywords['begin']:
            self.begin_statement()
        elif self.tokens and self.current_token.name != keywords['end']:
            #print "about to try prod_e\n"
            self.prod_E()
            self.match(symbols[';'])
    def if_statement(self):
        self.match(keywords['if'])
        print "matched if"
    def while_statement(self):
        self.match(keywords['while'])
        print "matched while"
    def for_statement(self):
        self.match(keywords['for'])
        print "matched for"
    def repeat_statement(self):
        self.match(keywords['repeat'])
        print "matched repeat"
    def assignment(self, lhs):
        print "matched Assignment"
        rhs = self.prod_L()
        #rhs = self.typematcher(self.previous_token.value, rhs)
        self.codes.append((opcodes['pop'], self.symboltable.index(lhs.value)))
        #self.codes.append((opcodes['pop'], self.previous_token.value))
    def typematcher(self, lhs, rhs):
        if type(lhs) == type(rhs):
            return rhs
        elif type(lhs) == int and type(rhs)== float:
            return int(rhs)
        elif type(lhs) == float and type(rhs) == int:
            return float(rhs)
        else:
            print "Error not same type"
            exit(0)
    def if_stat(self):
        pass
