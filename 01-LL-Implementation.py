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
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp


    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self):

        res = None
        if self.length == 1:
            res = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return res
        elif self.length == 0:
            return None
        else:
            res = self.head
            self.head = self.head.next
            self.length -= 1
            return res

    def get(self, index):

        if index >= self.length or index < 0:
            return None
        else:
            res = self.head
            for _ in range(index):
                res = res.next
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
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
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
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
           after = temp.next
           temp.next = before
           before = temp
           temp = after

        


my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)

my_linked_list.prepend(3)
my_linked_list.prepend(2)
my_linked_list.prepend(1)
my_linked_list.prepend(0)
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()


