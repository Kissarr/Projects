'''
def kaprekar_loop(L):
    while L != 6174:
        print(L)
        x = L // 1000
        y = (L // 100) % 10
        z = (L // 10) % 10
        b = L % 10
        L = [x, y, z, b]
        z = sorted(L)
        min = (str(z[0]) + str(z[1]) + str(z[2]) + str(z[3]))
        max = (str(z[3]) + str(z[2]) + str(z[1]) + str(z[0]))
        L = int(max) - int(min)
    print(L)


kaprekar_loop(L)
'''

def numerics(n):
    x = n // 1000
    y = (n // 100) % 10
    z = (n // 10) % 10
    b = n % 10
    return [x, y, z, b]

def kaprekar_step(L):
    z = sorted(L)
    min = (str(z[0])+str(z[1])+str(z[2])+str(z[3]))
    max = (str(z[3]) + str(z[2]) + str(z[1]) + str(z[0]))
    return int(max) - int(min)

def kaprekar_loop(n):
    if n == 1000:
        print ("Ошибка! На вход подано число 1000")
    elif n == 1111 or \
            n == 2222 or \
            n == 3333 or \
            n == 4444 or \
            n == 5555 or \
            n == 6666 or \
            n == 7777 or \
            n == 8888 or \
            n == 9999:
        print("Ошибка! На вход подано число " + str(n) + " - все цифры одинаковые")
    else:
        while n != 6174:
            print(n)
            n = (kaprekar_step(numerics(n)))
        else:
            print(n)


kaprekar_loop(1000)


