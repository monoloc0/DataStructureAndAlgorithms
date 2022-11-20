def print_items(n):
    """


    """
    for i in range(n):                  # O(n^2)
        for j in range(n):
            print(i,j)
    
    for k in range(n):                  # O(n)
        print(k)



"""
O(n²) + O(n)   -->    O(n²)    because  O(n²) is more dominant ---> Dropping Non-Dominants

"""


if __name__ == "__main__":
    print_items(10)

