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

    def BFS(self):

        current_node = self.root
        queue = []
        queue.append(current_node)
        results = []

        while len(queue)>0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results


    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)   

        traverse(self.root)
        return results

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

# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)


# print('Minimum Value in Tree:')
# print( my_tree.min_value_node(my_tree.root).value )


# ####### Test BFS #######
# """
#     EXPECTED OUTPUT:
#     ----------------
#     [47, 21, 76, 18, 27, 52, 82]

#  """
# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)

# print(my_tree.BFS())


####### Test DFS PreOrder #######

# """
#     EXPECTED OUTPUT:
#     ----------------
#     [47, 21, 18, 27, 76, 52, 82]

#  """

# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)

# print(my_tree.dfs_pre_order())



# ####### Test DFS PostOrder #######
# """
#     EXPECTED OUTPUT:
#     ----------------
#     [18, 27, 21, 52, 82, 76, 47]

#  """
# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)

# print(my_tree.dfs_post_order())


####### Test DFS InOrder #######
"""
    EXPECTED OUTPUT:
    ----------------
    [18, 21, 27, 47, 52, 76, 82]

 """

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_in_order())