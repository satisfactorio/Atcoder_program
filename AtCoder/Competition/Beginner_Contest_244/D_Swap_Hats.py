s1, s2, s3 = input().split()
t1, t2, t3 = input().split()
different_count = 0
if s1 != t1:
    different_count += 1
if s2 != t2:
    different_count += 1
if s3 != t3:
    different_count += 1
if different_count == 2:
    print('No')
else:
    print('Yes')