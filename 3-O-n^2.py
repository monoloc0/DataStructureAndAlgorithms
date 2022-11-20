def print_items(n):
    """

    O(n^2)

    """
    for i in range(n):
        for j in range(n):
            print(i,j)
    


if __name__ == "__main__":
    print_items(10)

