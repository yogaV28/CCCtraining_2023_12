n = int(input())
m = []
for i in range(n):
    m.append([x for x in input().split()])
    
for i in range(n):
    for j in range(n-i-1):
        if int(m[j][1]) > int(m[j+1][1]):
            m[j], m[j+1] = m[j+1], m[j]
        elif int(m[j][1]) == int(m[j+1][1]):
            if m[j][0] > m[j+1][0]:
                m[j], m[j+1] = m[j+1], m[j]
                
for i in range(n):
    print(m[i][0],m[i][1])
