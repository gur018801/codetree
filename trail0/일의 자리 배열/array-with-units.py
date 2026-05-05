a, b = map(int, input().split())
print(a, end=' ')
print(b, end=' ')
for i in range(8):
    c = (a + b)%10
    print(c, end=' ')
    a = b
    b = c