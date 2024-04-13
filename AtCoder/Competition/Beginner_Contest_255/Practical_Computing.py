import copy 
n = int(input())

    
def main(n, a = [1], answer = [[1]]):
    b = copy.deepcopy(a)
    if n == 0:
        return answer
    elif len(a) == 1:
        a.append(1)
        n -= 1
        answer.append(a)
        return main(n, a)
    else:
        for i in range(len(a) - 1):
            b.insert(i + 1, a[i] + a[i + 1])
            if i != len(a) - 2:
                b.pop(i + 2)
        n -= 1
        answer.append(b)
        return main(n, b)

answer = main(n - 1)
for ans in answer:
    print(*ans)

        
    