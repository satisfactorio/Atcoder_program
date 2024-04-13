import bisect

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
        index = bisect.bisect_left(height_list, height)
        print(student_total_number - index)
    