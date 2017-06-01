# PART 1 : Simple class object
class MyClass():
    "This is practice class"
    i = 12345
    def f(self):
        return "This is a simple class"

# attribute references
print MyClass.i
print MyClass.f
print MyClass.__doc__

#instantiation.
x = MyClass() # creates a new instance of the class and assigns this object to the local variable x.
print x.i
print x.f()
print x.__doc__

# PART 2 : customize class with __ini__ method
class MyClassCustom():
    def __init__(self,exp,salary):
        self.exp = exp
        self.salary = salary

y = MyClassCustom(5,10000)
print y.exp
print y.salary

# there are two kind of valid attributes names in class. 1) Data attribute 2) Method attribute

a = x.f  # a is method object and it can be called later in code
i=0
while i<5:
    print a()
    i = i+1

# PART 3 : Class and Instance Variables

#case 1 :
class football:
    player = "messi"
    def __init__(self,team):
        self.team = team

a = football('MANU')
b = football ('RM')
print a.player
print b.player
print a.team
print b.team

#case 2 :
class cricket:
    players = []
    def __init__(self,name):
        self.name = name
    def add_player(self,player):
        self.players.append(player)

w = cricket('Sachin')
z = cricket('ABD')
w.add_player('GANGULLY')
z.add_player('DHONI')
print w.players
print z.players

#case 3:

class cricket1:
    def __init__(self,name):
        self.name = name
        self.players = []

    def add_player(self,player):
        self.players.append(player)

q = cricket1('Gavasker')
a = cricket1('Kapil')
q.add_player("kholi")
a.add_player("smith")
print q.players
print a.players


# Part 4 : Derived class and base class

class pratik:
    def name(self):
        print "My name is PRATIK"
    def sport(self):
        print "I love football"


class zalak(pratik):
    def name(self):                     # here name method override another same name method form parant class PRATIK
        print "My name is Zalak"

    def salary(self):
        print "Hiiiiiiiiii"

x = pratik()
y = zalak()

print x.name()
print y.name()
#print x.salary()
print y.salary()
print y.sport()

