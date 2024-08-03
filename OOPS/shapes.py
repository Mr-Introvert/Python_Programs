class box:
    def __init__(self):
        self.length = float(input("Enter Length "))
        self.breadth = float(input("Enter Breadth "))
        self.width = float(input("Enter Width "))

    def area(self):
        ar = 2*((self.length*self.breadth)+(self.breadth*self.width)+(self.width*self.length))
        print(f"Surface Area is {ar}")

    def volume(self):
        vol = self.length*self.breadth*self.width
        print(f"Volume is {vol}")
bx=box()
bx.area()
bx.volume()