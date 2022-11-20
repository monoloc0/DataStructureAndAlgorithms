class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    
    def append(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def pop(self):

        res = None
        if self.length == 1:
            self.tail = None
            self.head = None
            self.length = 0
        elif self.head is None:
            return None
        else:
            temp = self.head

            while temp.next.next is not None:
                temp = temp.next
            
            self.tail = temp
            res = self.tail.next
            self.tail.next = None
            self.length -= 1
            return res.value

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

my_linked_list = LinkedList(4)
# my_linked_list.append(5)
# my_linked_list.append(6)
# my_linked_list.append(7)
# my_linked_list.append(8)

# my_linked_list.prepend(3)
# my_linked_list.prepend(2)
# my_linked_list.prepend(1)
my_linked_list.pop()
my_linked_list.prepend(1)
my_linked_list.prepend(2)
print(my_linked_list.length)

my_linked_list.print_list()