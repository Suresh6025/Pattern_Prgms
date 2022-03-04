N = int(input())
i = 1
while i <= N:
    j = 1
    strt_chr = chr(ord('A') + N - (i))
    while j <= i:
        out_chr = chr(ord(strt_chr) + j - 1)
        print(out_chr, end='')
        j = j + 1
    print()
    i = i + 1
