"""
Solutions to module 2 - A calculator
Student: David Hovstadius
Mail: david@hovstadius.com
Reviewed by: Oliver Groth
Reviewed date: 19/9-2022
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from pickletools import float8
from tokenize import TokenError
from unittest import result
from xml.dom.expatbuilder import parseString  
from MA2tokenizer import TokenizeWrapper
from MA1 import fib
from MA1 import fac
from statistics import mean

class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)



def statement(wtok, variables):
    """ See syntax chart for statement"""
    if not wtok.is_at_end():
         result = assignment(wtok, variables)
         if not wtok.is_at_end():            
            raise SyntaxError("Expected end of line")         
    return result



def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=' and wtok.has_next():
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
            wtok.next()
        else: 
            raise SyntaxError("Expected name")
    return result 
        


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        else:
            wtok.next()
            result = result - term(wtok, variables)
    return result



def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/': 
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)
        else:
            wtok.next()
            fak = factor(wtok,variables)
            if fak == 0:
                raise EvaluationError("Divison by 0")
            result = result / fak
    return result


def factor(wtok, variables):
    """ See syntax chart for factor"""
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()


    elif wtok.get_current() in function_1:
        a = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '(':
            wtok.next()
            argu = assignment(wtok,variables)
            if a == 'log' and argu <= 0:
                raise EvaluationError("Argument must be positive")
            elif (a == 'fib' or a == 'fac') and (not argu.is_integer() or argu < 0):
                raise EvaluationError("Argument must be a positivte integer")
            else:
                result = function_1[a](argu)
                wtok.next()
              
        else:
            raise SyntaxError("Expected '('")



    elif wtok.get_current() in function_n:
        b = function_n[wtok.get_current()]
        wtok.next()
        result = b(arglist(wtok,variables))
        
    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()
        else:
            raise EvaluationError("Not defined")


    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result = -1 * factor(wtok, variables)

    else:
        raise SyntaxError("Expected number or '('")  
    return result


def arglist(wtok,variables):
    """ See syntax chart for arglist"""
    if wtok.get_current() == '(':
        wtok.next()
        result = [assignment(wtok, variables)]
        while wtok.get_current() == ',':
            wtok.next()
            result = result + [assignment(wtok,variables)]
        if wtok.get_current() == ')':
            wtok.next()
        else: 
          raise SyntaxError("Expected ')' or ','")
    else:
        raise SyntaxError("Expected '('")
    return result

function_1 = {"sin": math.sin, "cos": math.cos, "exp": math.exp, "log": math.log, "fib": fib, "fac": fac}
function_n = {"min": min, "max": max, "sum": sum, "mean": mean}
         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()

        elif wtok.get_current() == 'vars':
            print(variables)

        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

            except EvaluationError as ee:
                print("*** Evaluation error:", ee)
                print(' ')
 


if __name__ == "__main__":
    main()
