class colour :
    colorindex = 0
    col = "Orange"
    def changecolour (self) :
        if self.col == "Orange" :
            self.col = "Blue"
        elif self.col == "Blue" :
            self.col = "Red"
        elif self.col == "Red" :
            self.col = "Yellow"
        elif self.col == "Yellow" :
            self.col = "Orange"
        print(self.col)
        self.colorindex = self.colorindex + 1
        print(self.colorindex)

color = colour()

print(type(color))
print(dir(color))
