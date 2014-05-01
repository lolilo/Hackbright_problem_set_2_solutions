from ps2 import *

# construct tree; see if you get desired result
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)
thirteen = Node(13)
fourteen = Node(14)

root = eight
root.insert(three)
root.insert(one)
root.insert(six)
root.insert(four)
root.insert(seven)
root.insert(ten)
root.insert(fourteen)
root.insert(thirteen)

# root.dft_preorder()
# print ''
# root.dft_postorder()
# print ''
# root.dft_inorder()
# print ''
# root.bft()
# root.bft_by_level()

# print root.height()
print root.balanced()