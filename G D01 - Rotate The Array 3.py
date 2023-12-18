# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
li=[int(i) for i in input().split()]
rotate=int(input())

rotate=rotate%n

for i in range(n):
    if i<rotate:
        print(li[n+i-rotate],end=' ')
    else:
        print(li[i-rotate],end=' ')
