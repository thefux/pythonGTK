class hello:
    
    def __init__(self, name):
        self.name = name

    def printName(self):
        return self.name

    name = ""

class world(hello):
    
    def __init__(self, name, age):
        hello.__init__(self, name)
        self.age = age

    def printAge(self):
        return "%s at the age of %d" %(self.name, self.age)


# h = hello("Abderrahmen")
# print h.printName()

w = world("Abderrahmen", 23)
print w.printAge()
