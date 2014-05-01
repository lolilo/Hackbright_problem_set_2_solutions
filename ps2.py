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
    def insert_as_degenerate(self, node): # basically a linked list
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

    def insert(self, node):
        if node.val < self.val:
            if not self.left:
                self.left = node
            else: # see where to insert new node past the existing node, recursively
                self.left.insert(node)
        else: # node.val >= self.val
            if not self.right:
                self.right = node
            else:
                self.right.insert(node)
    """Dear Christian, implementing these as methods feels clunky...I'd prefer them as external functions."""
    def dft_preorder(self):
        print self.val
        if self.left:
            self.left.dft_preorder()
        if self.right:
            self.right.dft_preorder()

    def dft_postorder(self): # application: evaluate a parse tree
        if self.left:
            self.left.dft_postorder()
        if self.right:
            self.right.dft_postorder()
        print self.val

    def dft_inorder(self): # application: convert parse tree back to original expression
        if self.left:
            self.left.dft_inorder()
        print self.val
        if self.right:
            self.right.dft_inorder()

    def bft(self): 
        thislevel = [self]
        while thislevel:
            nextlevel = []
            for node in thislevel:
                print node.val
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            thislevel = nextlevel

    def bft_by_level(self): 
        thislevel = [self]
        while thislevel:
            nextlevel = []
            for node in thislevel:
                print node.val,
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            thislevel = nextlevel
            print ''

    """Super clunky. This would be shorter if it were an external function and I could pass in None."""
    def height(self):
        if (not self.left) and (not self.right):
            return 1
        elif self.right and self.left:
            return 1 + max(self.left.height(), self.right.height())
        elif self.right:
            return 1 + self.right.height()
        elif self.left:
            return 1 + self.left.height()

    def balanced(self):
        # if height of tree is <= 2, it is balanced by definition
        if self.height() <= 2:
            return True

        unbalanced_left = (self.left and not self.right) and (self.left.left or self.left.right)
        unbalanced_right = (self.right and not self.left) and (self.right.left or self.right.right)
        if unbalanced_left or unbalanced_right:
            return False

        return self.left.balanced() and self.right.balanced()

"""
5. Write a function that, given two binary trees, returns a boolean indicating whether or not the trees have identical structure and value (ie: are they the same tree).
"""

def identical_trees(tree1, tree2):
    if not tree1 and not tree2:
        return True

    only_one_tree = (tree1 and not tree2) or (not tree1 and tree1)

    only_left_branch = (tree1.left and tree2.left) and (not tree1.right and not tree2.right)
    only_right_branch = (tree1.right and tree2.right) and (not tree1.left and not tree2.left)
    both_branches = (tree1.right and tree1.left) and (tree2.right and tree2.right)
    # WHY DID THESE BOOLEANS NOT WORK? 

    def only_left(tree1, tree2):
        if (tree1.left and tree2.left) and (not tree1.right and not tree2.right):
            return True
        return False

    def only_right(tree1, tree2):
        if (tree1.right and tree2.right) and (not tree1.left and not tree2.left):
            return True
        return False

    def both_branches(tree1, tree2):
        if (tree1.right and tree1.left) and (tree2.right and tree2.right):
            return True
        return False

    # print 'left branch', only_left_branch
    # print 'right branch', only_right_branch
    # print 'both', both_branches

    trees_of_same_size = only_left_branch or only_right_branch or both_branches
    # print trees_of_same_size

    if trees_of_same_size:
        print 'trees are the same size'
        print tree1.val, tree2.val

    if only_one_tree or not trees_of_same_size:
        print ''
        print 'left branch', only_left(tree1, tree2)
        print 'right branch', only_right_branch
        print 'both', both_branches
        print 'not trees_of_same_size', not trees_of_same_size
        print 'only_one_tree', only_one_tree
        print tree1.val
        print tree2.val
        return False

    # At this point, we know they have the same stucuture. We need to check values now.
    if tree1.val != tree2.val:
        return False
    return identical_trees(tree1.left, tree2.left) and identical_trees(tree1.right, tree2.right)
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

