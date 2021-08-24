def dec(func):
    def wrapper():
        print("Код перед")
        func()
        print("Код после")

    return wrapper

x = int(input())
@dec
def show():
    st = x**2
    print(st)

show()
