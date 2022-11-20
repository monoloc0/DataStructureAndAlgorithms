def print_items(a,b):       # O(a)
    for i in range(a):
        print(i)

    for j in range(b):      # O(b)
        print(j)


                            # that results in O(a+b) because a and b have different values. Those 2 values can't be simplified to just on variable