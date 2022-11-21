class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) *23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print("{}:{}".format(i, val))

    def set_item(self, key, value):
        index = self.__hash(key)

        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)

        if self.data_map[index] is None:
            return None

        for i in self.data_map[index]:
            if i[0] == key:
                return i[1]
        
        return None

    def keys(self):
        all_keys = []

        for i in self.data_map:
            if i is not None:
                for k in i:
                    all_keys.append(k[0])
        
        return all_keys




### Test Set ###

# my_hash_table = HashTable()

# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)
# my_hash_table.set_item('lumber', 70)

# my_hash_table.print_table()



"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  [['bolts', 1400], ['washers', 50]]
    5 :  None
    6 :  [['lumber', 70]]

"""




### Test Get ###

# my_hash_table = HashTable()

# my_hash_table.set_item('bolts', 1400)
# my_hash_table.set_item('washers', 50)

# print('Bolts:', my_hash_table.get_item('bolts'))
# print('Washers:', my_hash_table.get_item('washers'))
# print('Lumber:', my_hash_table.get_item('lumber'))


### Test keys() ###

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())