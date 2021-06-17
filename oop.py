s= "helo"
print(dir(s))
print(help(s.upper()))
print(s.upper())
print((5555).bit_length())

#Classes and methods constractors and how to acess the variables and methods
class Patient:
    def __init__(self, name, age, malady):
        self.name = name
        self.age = age
        self.malady =malady

    def display(self):
        """Display the Patient’s attributes."""
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Malady = ", self.malady)


    def cure(self):
        self.malady = "healthy"



ahmad =Patient("ahmad droobi",22, "hasjndk")
print(ahmad.display())
ahmad.cure()
print(ahmad.display())


##############################################
# operator overloading

s1 = "hi "+ "its ahamd " # concat()
print(s1)
s2 ="$$"*70  #repetition # note the number must be integer if its float or something like this it make type error
print(s2)

s3 = 10*"%%"+"Done" #Both concat +repeat
print(s3)



