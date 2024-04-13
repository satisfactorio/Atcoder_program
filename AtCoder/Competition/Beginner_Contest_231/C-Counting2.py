def binary_search(array, search_value):
    lower_bound = 0
    upper_bound = student_total_number - 1

    while 1 < upper_bound - lower_bound:
        if (upper_bound + lower_bound) % 2 == 1: 
            midpoint = (upper_bound + lower_bound - 1) // 2
        else:
            midpoint = (upper_bound + lower_bound) // 2
        
        value_at_midpoint = array[midpoint]

        
        if search_value <= value_at_midpoint:
            upper_bound = midpoint
        elif search_value > value_at_midpoint:
            lower_bound = midpoint
    
    return upper_bound
        

student_total_number, height_index = map(int, input().split())
height_list = list(map(int, input().split()))
height_list.sort()

for i in range(height_index):
    height = int(input())
    if height > height_list[student_total_number - 1]:
        print(0)
    elif height < height_list[0]:
        print(student_total_number)
    else:
        index = binary_search(height_list, height)
        print(student_total_number - index)




    
