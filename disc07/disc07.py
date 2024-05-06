# Question 1.1
class Student:
    students = 0 # this is a class attribute 
    def __init__(self, name, staff):
        self.name = name # this is an instance attribute 
        self.understanding = 0 
        Student.students += 1 
        print("There are now", Student.students, "students") 
        staff.add_student(self) 
    
    def visit_office_hours(self, staff): 
        staff.assist(self) 
        print("Thanks, " + staff.name)
            

class Professor:
    def __init__(self, name): 
        self.name = name 
        self.students = {} 
    
    def add_student(self, student): 
        self.students[student.name] = student 
    
    def assist(self, student): 
        student.understanding += 1


callahan = Professor("Callahan")
elle = Student("Elle", callahan)
elle.visit_office_hours(callahan)
elle.visit_office_hours(Professor("Paulette"))
elle.understanding
[name for name in callahan.students]
x = Student("Vivian", Professor("Stromwell")).name
x
[name for name in callahan.students]



# Question 1.2
class MinList:
    """only can pop smallest item"""
    
    def __init__(self):
        self.item = []
        self.size = 0
    
    def append(self, item):
        self.item.append(item)
        self.size += 1
        
    def pop(self):
        to_be_removed = min(self.item)
        for i in range(len(self.item)):
            if self.item[i] == to_be_removed:
                self.size -= 1
                return self.item.pop(i)
        else:
            assert False, "something is wrong."


m = MinList()
m.append(4)
m.append(1)
m.append(5)
m.size
m.pop()
m.size



# Question 1.3
class Email:
    """Every email object has 3 instance attributes: the message, the sender name, and the recipient name. """ 
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server: 
    """Each Server has an instance attribute clients, which is a dictionary that associates client names with client objects. """ 
    def __init__(self): 
        self.clients = {}
    
    def send(self, email): 
        """Take an email and put it in the inbox of the client it is addressed to. """
        recipient = email.recipient_name
        if recipient in self.clients:
            self.clients[recipient].receive(email)
        else:
            return "The recipient is not in our client list."
    
    def register_client(self, client, client_name): 
        """Takes a client object and client_name and adds them to the clients instance attribute. """
        self.clients[client_name] = client
    
    
class Client: 
    """Every Client has instance attributes name (which is used for addressing 
    emails to the client), server (which is used to send emails out to other clients),
    and inbox (a list of all emails the client has received). 
    """
    def __init__(self, server, name): 
        self.inbox = []
        self.name = name
        self.server = server
    
    def compose(self, msg, recipient_name): 
        """Send an email with the given message msg to the given recipient client. """
        self.server.send(Email(msg, self.name, recipient_name))
    
    def receive(self, email): 
        """Take an email and add it to the inbox of this client. """
        self.inbox.append(email)





# Question 2.1
class Pet:
    def __init__(self, name, owner):
        self.is_alive = True
        self.owner = owner
        self.name = name
    
    def eat(self, thing):
        print(f"{self.name} ate a {thing}!")
        
    def talk(self):
        assert False, "need to be defined."


class Dog(Pet):
    def talk(self):
        print(f"{self.name} says woof!")
    

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        #super().__init__(name, owner)
        Pet.__init__(self, name, owner)
        self.lives = lives
        
    def talk(self):
        print(f"{self.name} says meow!")
    
    def lose_life(self): 
        """Decrements a cat's life by 1. When lives reaches zero, 
        'is_alive' becomes False. If this is called after lives has 
        reached zero, print out that the cat has no more lives to lose. 
        """
        if self.is_alive:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print("The cat has no more lives to lose.")
            

pudding = Dog('pudding', 'me')
pudding.eat('food')
pudding.talk()

cat = Cat('cat', 'not me')
cat.talk()
cat.eat('food')

for _ in range(11):
    print(_)
    cat.lose_life()
    
    
    


# Question 2.2
class NoisyCat(Cat):
    """A Cat that repeats things twice."""
    
    """
    def __init__(self, name, owner, lives=9): 
        # Is this method necessary? Why or why not?
        # this methid is not necessary, since NoisyCat inherits it from Cat class
    """
    def talk(self): 
        """Talks twice as much as a regular cat. 
        >>> NoisyCat('Magic', 'James').talk() 
        Magic says meow! 
        Magic says meow! 
        """
        super().talk()
        Cat.talk(self)
    
    def __repr__(self): 
        """The interpreter-readable representation of a NoisyCat
        
        >>> muffin = NoisyCat('Muffin', 'Catherine')
        >>> repr(muffin) 
        "NoisyCat('Muffin', 'Catherine')"
        >>> muffin 
        NoisyCat('Muffin', 'Catherine')
        """
        
        return f"NoisyCat('{self.name}', '{self.owner}')"