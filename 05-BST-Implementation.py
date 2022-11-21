class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None
        
    def insert(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return True
        
        temp = self.root

        while True:
            if temp.value == value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        if self.root == None:
            return False

        temp = self.root

        while temp is not None:
            if temp.value == value:
                return True
            
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        
        return current_node


####### Test Insert #######
# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)


# print('Root:', my_tree.root.value)            
# print('Root->Left:', my_tree.root.left.value)        
# print('Root->Right:', my_tree.root.right.value)        

####### Test Contains #######
# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)

# print('BST Contains 27:')
# print(my_tree.contains(27))

# print('\nBST Contains 17:')
# print(my_tree.contains(17))

####### Test min_value_node #######

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print('Minimum Value in Tree:')
print( my_tree.min_value_node(my_tree.root).value )

            

"""
    EXPECTED OUTPUT:
    ----------------
    Minimum Value in Tree:
    18

"""
