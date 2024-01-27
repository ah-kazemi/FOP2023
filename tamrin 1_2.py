n = int(input())
m = int(input())
k = int(input())

while(n != 0):
    carry = m & n
    m = m ^ n
    n = carry << 1
print (m)
if m == k:
    print("YES")
else:
    print("NO")