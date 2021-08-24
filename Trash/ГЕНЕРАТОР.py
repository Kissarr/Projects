def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i


mygenerator = createGenerator()  # создаём генератор
print(mygenerator)  # mygenerator является объектом!

for i in mygenerator:
    print(i)

for i in mygenerator:
    print(i)
