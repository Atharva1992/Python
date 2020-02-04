class partyanimal :
    x = 0
    name = ""
    def func1 ():
        print("Atharv1")
    def func2 ():
        print("Atharv2")
    def func3 ():
        print("Atharv3")

class lameanimal(partyanimal) :
    y = 0
    surname = ""
    def func4 ():
        print("Atharv1")
    def func5 ():
        print("Atharv2")
    def func6 ():
        print("Atharv3")


man1 = partyanimal()
print(type(man1))
print(dir(man1))
man2 = lameanimal()
print(type(man2))
print(dir(man2))
