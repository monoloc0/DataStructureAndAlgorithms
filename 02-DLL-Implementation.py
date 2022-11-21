class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            res = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return res

        res = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        res.prev = None
        self.length -= 1
        return res

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        
    
    def pop_first(self):

        if self.length == 0:
            return None
        
        res = self.head
        if self.length == 1:
            
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            res.next = None
        self.length -= 1
        return res

    def get(self, index):

        if index >= self.length or index < 0:
            return None
        res = self.head
        if index < self.length/2:
            for _ in range(index):
                res = res.next
        else:
            res = self.tail
            for _ in range((self.length-1) - index):
                res = res.prev
        return res


    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        
        prev = self.get(index - 1)
        temp = prev.next
        new_node.next = temp
        new_node.prev = prev
        prev.next = new_node
        temp.prev = new_node
        self.length += 1   
        return True  


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return False
        if self.length == 1 and index == 0:
            self.head = None
            self.tail = None
            return True
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
            
        prev = self.get(index-1)
        after = prev.next
        prev.next = after.next
        after.next.prev = prev
        after.next = None
        after.prev = None
        self.length -= 1
        return after


my_doubly_linked_list = DoublyLinkedList(1)

my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(6)
my_doubly_linked_list.append(7)

my_doubly_linked_list.prepend(0)

#print(my_doubly_linked_list.length)

my_doubly_linked_list.remove(3)

my_doubly_linked_list.print_list()

