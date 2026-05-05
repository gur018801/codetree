N = int(input())
a = list(map(int, input().split()))

for i in range(N - 1, -1, -1):
    if a[i] % 2 == 0:
        print(a[i], end=' ')