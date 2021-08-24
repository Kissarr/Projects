def numerics(n):
    x = n // 1000
    y = (n // 100) % 10
    z = (n // 10) % 10
    b = n % 10

    print([x, y, z, b])


numerics(n)
