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
            l = l[:i]
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

"""3. Implement a function that recursively computes the length of a list

    [1, 2, 3] -> 3"""

"""4. Binary search tree questions
    
    4.1 Define a class initializer that represents a binary tree node

    4.2 Write a method, .insert() that takes in a new value N and inserts it into an appropriate place in the binary search tree (ignore balance)

    4.3 Write a method, .dft() that enumerates the values of all the nodes in the tree using a depth-first traversal (recursive)
    
    4.4 Write a method, .bft() that enumerates the values of all the nodes in the tree using a breadth-first traversal (non-recursive)

    4.5 (GL4.1) Write a method, .balanced() that determines whether or not the tree is balanced and returns a boolean indicating the fact.
"""

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

