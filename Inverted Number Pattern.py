N = int(input())
i = 1
while i <= N:
    j = 1
    while j <= N-i+1:
        print(N-i+1, end = '')
        j = j + 1
    print()
    i = i + 1
