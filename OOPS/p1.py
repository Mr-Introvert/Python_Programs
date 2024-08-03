class Person:
    name = "Bijoy"
    occupation = "Software Developer"
    salary = 5000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.info()
a.name = "Rohit"
a.occupation = "Accountant"
a.info()