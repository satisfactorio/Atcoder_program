l, r = map(int, input().split())
s = input()

letter = s[l-1:r]
reverse = letter[::-1]

start = s[:l-1]
end = s[r:]

result = start + reverse + end
print(result)


    
