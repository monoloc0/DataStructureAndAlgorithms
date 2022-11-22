def bubble_sort(my_list):

    for i in range(1, len(my_list)):
        for j in range(len(my_list)-i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


my_list = [4,2,6,5,1,3]

print(bubble_sort(my_list))