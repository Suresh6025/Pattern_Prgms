n = int(input())

for i in range(1, n+1):
    for j in range(1, 2*(n+1)):
        if(i == j or j == n+1 or i == 2*(n+1)-j):
            print("*", end="")
        else:
            print( "0", end="")
    print()