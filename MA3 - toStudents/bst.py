""" bst.py

Student: David Hovstadius
Mail: david@hovstadius.com
Reviewed by: David Meadon
Date reviewed: 10/5 - 2022
"""


from ast import keyword
#from curses import resize_term
from linked_list import LinkedList
import random
import math

class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        r = self._size(self.root)
        return r

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    # def height(self,root):                             # Compulsory
    #     if root is None:
    #         return 0
    #     leftA = self.height(root.left)
    #     rightA = self.height(root.right)
    #     return max(leftA,rightA) + 1

    def height(self):
        return self._height(self.root)

    def _height(self,r):
        if r is None:  
            return 0
        else:
            Aleft = self._height(r.left)
            Aright = self._height(r.right)
            return 1 + max(Aleft,Aright)

            

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left,k)
        elif k > r.key:
            r.right =  self._remove(r.right,k)
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                tempr = r.right
                while tempr.left:
                    tempr = tempr.left                   
                tempkey = tempr.key
                r.key = tempkey
                r.right = self._remove(r.right,tempkey)
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def __str__(self):                            # Compulsory
        result = '<'
        if self.size() == 0:
            return result + '>'
        else:
            for i in (self.__iter__()):
                result += str(i) + ', '
            return result[:-2] + '>'




    def to_list(self):                            # Compulsory
        lst = []
        for i in self.__iter__():
            lst.append(i)
        return lst



    def to_LinkedList(self):                      # Compulsory
        lst = LinkedList()
        for i in self.__iter__():
            lst.insert(i)
        return lst

    def ipl(self):                                # Compulsory
        r = self.root
        lvl = 0
        return self._ipl(r,lvl)

    def _ipl(self,r,lvl):  # Internal path length, Definition is sum of of all nodes levels
        lvl += 1
        if r is None:
            return 0
        return lvl + self._ipl(r.left,lvl) + self._ipl(r.right,lvl)


def random_tree(n):                               # Useful
    t = BST()
    index = 0
    for index in range(n):
        t.insert(random.random())
        index += 1
    return t


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()
    # print('size  : ', t.size())
    # for k in [0, 1, 2, 5, 9]:
    #     print(f"contains({k}): {t.contains(k)}")

    print()
    n = 100000
    p = random_tree(n)

    print(p.height())
    print(p.ipl()/n)
    print(1.39*math.log(n,2))


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

__iter__ gives data not index 

1. computing size? good 
2. computing height? bad
3. contains? good
4. insert? bad 
5. remove? bad




Results for ipl of random trees
===============================

n = 10 gives:
ipl/n = 3.5
1.39*math.log(n,2) = 4.62
height = 7

n = 1000
ipl/n = 11.79
1.39*math.log(n,2) = 13.85
height = 23

n = 100000
ipl/n = 22.13
1.39*math.log(n,2) = 23.09
height = 42

The correlation between height and number of nodes is that the average height is
equal to twice the internal path length divided by number of nodes.

height = 2*ipl/n

"""
