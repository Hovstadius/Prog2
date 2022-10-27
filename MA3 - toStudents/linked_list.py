""" linked_list.py

Student: David Hovstadius
Mail: david@hovstadius.com
Reviewed by: David Meadon
Date reviewed: 10/5 - 2022
"""


from asyncio.windows_events import NULL
from http.client import EXPECTATION_FAILED
from logging import setLogRecordFactory
from msilib.schema import Error
from operator import getitem
from os import lstat
from re import A, S
from statistics import pstdev
from time import perf_counter, perf_counter_ns
from tkinter import N
from turtle import end_fill
from unittest.mock import NonCallableMagicMock


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):             # Optional
        counter = 0
        f = self.first
        while f:
            counter += 1
            f = f.succ
        return counter

    def mean(self):               # Optional
        sum = 0
        counter = 0
        f = self.first
        while f:
            sum += f.data
            counter += 1
            f = f.succ
        return (sum/counter)


    def remove_first(self):
        if self.first == None:
            return None
        result = self.first.data
        self.first = self.first.succ
        return result



    def remove_last(self):        # Optional
        if self.first == None:
            return None
        if self.first.succ == None:
            self.first = None
            return None
        f = self.first
        while f.succ.succ:
            f = f.succ
        f.succ = None
        

  
       
    def remove(self, x):          # Compulsory
        if self.first == None:
            return False
        elif self.first.succ == None:
            if self.first.data == x:
                self.first = None
                return True
            else:
                return False
        else:
            f = self.first
            while f is not None:
                a = f
                f = f.succ
                if a.data == x:
                    self.remove_first()
                    return True
                elif f.data == x:
                    a.succ = a.succ.succ
                    return True
                else:
                    return False
    

        

    def count(self, x):           # Optional
        pass



    def to_list(self):            # Compulsory
        result = []
        self._to_list(self.first,result)
        return result

    def _to_list(self,f,result):
        if f:
            result.append(f.data)
            self._to_list(f.succ,result)



    def remove_all(self, x):      # Compulsory        
        self.first = self._remove_all(x,self.first)
        return

    def _remove_all(self,x,f):
        if f == None:
            return None
        elif f.data == x:
            return self._remove_all(x,f.succ)
        else:
            f.succ = self._remove_all(x,f.succ)
            return f




    def __str__(self):            # Compulsary
        val = iter(self)
        s = '('
        while True:
            try:
                s += str(next(val))
                s += ', '
            except StopIteration:
                if len(s) == 1:
                    s += ')'
                else:
                    s = s[:-2]
                    s += ')'
                break
        return s



    def copy(self):               # Compulsary
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 

    complexity = O(n^2)
    where n is the number of nodes

    n^2 because insert goes through the whole list from start each time

    '''

    def copy(self):               # Compulsary, should be more efficient
        result = LinkedList()
        list = self.to_list()
        list.reverse()
        for x in list:
            result.insert(x)
        return result                  
        
        
    ''' Complexity for this implementation:

    complexity = O(n)
    where n is the number of nodes

    now it's only n because the insert is in reverse order, which is the best case,
    since it doesn't need to iterate to find the data to be inserted.


    '''


    
    def __getitem__(self, ind):   # Compulsory
        f = self.first
        count = 0
        while f:
            if count == ind:
                return f.data
            count += 1
            f = f.succ
        raise IndexError('Index larger than list')  


class Person:                     # Compulsory to complete
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __gt__(self,other):
        if type(other) != float:
            pass

        if self.pnr > other:
            return True
        else:
            return False

    def __lt__(self,other):
        if type(other) != float:
            pass
        
        if self.pnr < other:
            return True
        else:
            return False

    def __ge__(self,other):
        if type(other) != float:
            pass
        
        if self.pnr >= other:
            return True
        else:
            return False

    def __le__(self,other):
        if type(other) != float:
            pass
        
        if self.pnr <= other:
            return True
        else:
            return False

def main():
    lst = LinkedList()
    for x in [3, 1, 2, 6]:
        lst.insert(x)
    lst.print()
    # Test code:
    
    lst2 = LinkedList()
    per = Person('David',19990810)
    per2 = Person('Jon',9807231456)

    


    lst2.insert(per2)    
    lst2.insert(per)
    lst2.insert(Person('Oskos',99))
    lst2.print()
    


    

if __name__ == '__main__':
    main()
