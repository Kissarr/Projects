def is_prime(a):
    i = 2
    while i < a:
        if a % i == 0:
            print("False")
            return i
        else:
            i += 1
    print("True")

a = int(input("4islo "))
is_prime(a)