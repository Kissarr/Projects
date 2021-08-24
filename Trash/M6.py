def bank(a, year):
    while year > 0:
        a *= 1.1
        year -= 1
    print(a)


a = float(input("Summa "))
year = int(input("Dlitelnost let "))
bank(a, year)
