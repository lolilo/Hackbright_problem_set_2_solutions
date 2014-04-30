# Recursion, Search, Trees

"""1. Implement a function that takes in a list and a search term and searches the list for the term using a binary search

    [1, 2, 3, 4], 5 -> False
    [1, 2, 3, 4], 1 -> True
"""

def binary_search(l, target):
    while len(l) > 0:
        i = len(l)//2
        current_element = l[i]
        if target < current_element:
            l = l[:i] # slicing the list each time is expensive...how can we avoid this?
        elif target > current_element:
            l = l[i + 1:]
        else: 
            return True
    return False

"""1.1 Implement a binary search function recursively."""

def recursive_binary_search(l, target):
    if not l:
        return False
    
    middle = len(l)//2
    current_element = l[middle]
    if current_element == target:
        return True
    if target < current_element:
        return recursive_binary_search(l[:middle], target)
    else:
        return recursive_binary_search(l[middle + 1:], target)

"""2. Implement a function to compute the nth fibonacci number recursively.

    1 -> 1
    2 -> 2
    3 -> 3
    4 -> 5"""

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

"""2.1 Implement a function to print the fibonacci numbers up to n, inclusive."""

def print_fib(n):
    a, b = 1, 1
    print a
    print b
    for i in xrange(3, n + 1):
        print a + b
        temp = a
        a = b
        b += temp
# print_fib(10)

"""3. Implement a function that recursively computes the length of a list

    [1, 2, 3] -> 3"""

def recursive_length_of_list(l):
    if not l:
        return 0
    return 1 + recursive_length_of_list(l[1:])

"""4. Binary search tree questions
    
    4.1 Define a class initializer that represents a binary tree node

    4.2 Write a method, .insert() that takes in a new value N and inserts it into an appropriate place in the binary search tree (ignore balance)

    4.3 Write a method, .dft() that enumerates the values of all the nodes in the tree using a depth-first traversal (recursive)
    
    4.4 Write a method, .bft() that enumerates the values of all the nodes in the tree using a breadth-first traversal (non-recursive)

    4.5 (GL4.1) Write a method, .balanced() that determines whether or not the tree is balanced and returns a boolean indicating the fact.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def insert(self, node):
        if node.val < self.val:
            if not self.left:
                self.left = node
            else: # a node already exists
                # check if existing node < new node; if so, insert here
                if self.left.val < node.val:
                    node.left = self.left
                    self.left = node
                else: # see where to insert new node past the existing node, recursively
                    self.left.insert(node)
        else: # node.val >= self.val
            if not self.right:
                self.right = node
            else: 
                if self.right.val > node.val:
                    node.right = self.right
                    self.right = node
                else:
                    self.right.insert(node)
    def dft_preorder(self):
        print self.val
        if self.left:
            self.left.dft_preorder()
        if self.right:
            self.right.dft_preorder()
    def dft_postorder(self):
        if self.left:
            self.left.dft_postorder()
        if self.right:
            self.right.dft_postorder()
        print self.val


    
# construct tree; see if you get desired result
root = Node(8)
five = Node(5)
seven = Node(7)
six = Node(6)
eight = Node(8)
nine = Node(9)
ten = Node(10)

# print root.val
root.insert(five)
# print root.left.val
root.insert(six)
# print root.left.val
root.insert(eight)
# print root.left.val, root.right.right.val
root.insert(seven)
# print root.left.val, root.right.right.right.val
root.insert(nine)
root.insert(ten)
root.dft_postorder()

"""
5. Write a function that, given two binary trees, returns a boolean indicating whether or not the trees have identical structure and value (ie: are they the same tree).
"""

"""
6. Write a function that takes in a randomly ordered list and reorganizes the list as follows: take the first element in the list to be the 'dividing line'. Move all elements in the list that are smaller than the first element to the left of it, and all elements greater to the right.

    [5, 9, 1, 3, 7, 6, 2] -> [1, 3, 2, 5, 9, 7, 6]
    [2, 3, 1] -> [1, 2, 3]
"""

"""
7. Write a function that takes in a list of integers and a target number. The function should return a list of tuples, each tuple containing a pair of numbers from the original list that add up to zero. Do not use a number more than once.

    [1, 2, 3, 4, 0], 3 -> [(1,2), (3,0)]
    [0, 0, -1, 1, 0, 1, -1], 0 -> [(0, 0), (-1, 1), (1, -1)]
"""

