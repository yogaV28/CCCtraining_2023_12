n = int(input())
worth = list(map(int,input().split()))
q, x = map(int, input().split())
bag = []
coin = 0
ans = -1
for i in range(q):
    cmd = input()
    if cmd == "Harry":
        bag.append(worth[coin])
        coin += 1
    if cmd == "Remove":
        if bag != []:
            del bag[len(bag)-1]
    if sum(bag) == x:
        ans = len(bag)
        break
print(ans)
