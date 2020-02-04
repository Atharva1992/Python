class newmember :
    x = 0
    name = ""

    def __init__ (self,z):
        print("Constructed")
        self.name = z

    def __del__ (self):
        print("Deconstructed")

ab = newmember("Atharva")
print("Hello World",ab.name)

x = 45
