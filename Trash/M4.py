"""
i = int(input())
a = 1
b = 1
while a<=i:
    for x in range(i):
        for p in range(b):
            print(a, end=" ")
            b +=1
        a += 1
"""
num = int(input())

for i in range(1, num+1):
    for q in range(1, i+1):
        print(q, end="")
    for a in range(i, 1, -1):
        print(a-1, end="")
    print("")