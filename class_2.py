class student:
    grade = 10
    name = "Penguin"

    def introduction(self):
        print("Hi, I am a student")
    
    def details(self):
        print("My name is", self.name)
        print("I am in year", self.grade)

op = student()
op.introduction()
op.details()