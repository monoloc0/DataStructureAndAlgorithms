def print_items(n):
    """
    O(2n) --> O(n)   

    The constant "2" can just be dropped

    """
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


if __name__ == "__main__":
    print_items(10)

