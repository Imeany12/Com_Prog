# -*- coding: utf-8 -*-
"""Copy of Lecture12_Class.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IMwVzpoxOvy0aRiYz0JvPqFqjsv1QWe7

# **Lecture12: Class & Objects in Python**

![animation](https://c.tenor.com/bQCHJwgCNuMAAAAC/kitten-cat.gif)

# Part1: Introduction

Each book contains name (title), ISBN, and price.<br>
If we have many books, what should we do?
"""

name1 = "Data Science"
ISBN1 = "149190142X"
price1 = 28.79

name2 = "Learning Python"
ISBN2 = "1449355730"
price2 = 37.06

name3 = "Data Analysis"
ISBN3 = "1449319793"
price3 = 27.68

#------------------------------------
# Solution1: tuple
#------------------------------------

# ----- functions -----
def total_price( books ):
   s = 0
   for b in books:
       s += b[2]
   return s

# ----- main -----
b1 = ("Data Science",    "149190142X", 28.79)
b2 = ("Learning Python", "1449355730", 37.06)
b3 = ("Data Analysis",   "1449319793", 27.68)
books =  [b1, b2, b3]
print(total_price( books ))

#------------------------------------
# Solution2: dict
#------------------------------------

# ----- functions -----
def total_price( books ):
   s = 0
   for b in books:
       s += b["price"]
   return s

# ----- main -----
b1 = {"title":"Data Science", "isbn":"1408142X", "price": 28.79} 
b2 = {"title":"Easy Python",  "isbn":"14455730", "price": 37.06}
b3 = {"title":"Big Data",     "isbn":"14493793", "price": 27.68}
books = [b1, b2, b3]
print(total_price( books ))

"""A **class** is a code template for creating objects. You can also think of class as user-defined data type. 

**Objects** are variables created from class (template).
"""

#------------------------------------
# Solution3: Class
# https://pythontutor.com/ 
#------------------------------------

# ----- class -----
class Book:
   # this is also called "constructor" - how to create object!
   def __init__(self, title, isbn, price):
      self.title = title
      self.isbn  = isbn
      self.price = price

# ----- main -----
# create 3 books (objects) with one class (Book)
b1 = Book("Data Science",   "149190142X", 28.79)
b2 = Book("Learning Python","1449355730", 37.06)
b3 = Book("Data Analysis",  "1449319793", 27.68)

print(b1.title, b1.isbn, b1.price)

"""##Exercise1: Student class (v1)

Create Student class, where each student contains ID and name. Also, create two students (objects).
"""

# ----- class -----
class Student:

  def __init__(self, id, name) :
    self.id = id
    self.name = name
  
# ----- main -----
s1 = Student("6538083121","Paopao")
print(s1.id,s1.name)

#@title solution
# ----- class -----
# https://pythontutor.com/
class Student:
   def __init__(self, ID, name):
     self.ID = ID
     self.name = name

# ----- main -----
s1 = Student("6438027021", "Mark Zuckerberg")
s2 = Student("6438073821", "Lisa Blackpink")

"""#Part2: Sample Basic Classes

There are 6 sample classes.<br>
"""

# Sample1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

p = Point(10, 23)

# Sample2
class Date:
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

d = Date(14, 2, 2021)

# Sample3
class Song:
    # There are 4 properties, but user just needs to define only 3 inputs.
    def __init__(self, title, artist, lyrics):
        self.title  = title
        self.artist = artist
        self.lyrics = lyrics
        self.nviews = 0

x = Song("Hello", "Adele", "")
print(x.nviews)

# Sample4
class BankAccount:
    def __init__(self, acc_no, acc_name, balance):
        self.acc_no   = acc_no
        self.acc_name = acc_name
        self.balance  = balance

b = BankAccount("101", "Peerapon", 1000)

# Sample5
class Rectangle:
    def __init__(self, lower_left, w, h):
        self.lower_left = lower_left # class Point
        self.height = h
        self.width  = w

pp = Point(1,2)

r = Rectangle(pp, 4, 5)

print(r.lower_left.x)
print(r.lower_left.y)

# Sample6
class Course:
    # There are 3 properties, but user just needs to define only 2 inputs.
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.students = [] # empty list

c1 = Course("2190101", "Computer Programming")

"""<font color=red>Unlike Java, Python doesn't support overloading methods, two methods the same names.</font>"""

# After uncomment, can we run this code?
class Point3D:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.z = 0
    
    # def __init__(self, x, y, z):
    #     self.x = x
    #     self.y = y 
    #     self.z = z

p = Point3D(10, 23)

"""##Exercise2: Student class (v2)

Update Student class in Exercise1 to 3 properties including ID, name, score. Create a constructor with two user-defined inputs: ID & name, where score is initiazed with 0.
"""

# ----- class -----
class Student:
   def __init__(self,ID,name,score) :
     self.ID = ID
     self.name = name
     self.score = 0

# ----- main -----
s1 = Student("6538083121","Paopao","")
print(s1.score)

#@title solution
# ----- class -----
# https://pythontutor.com/
class Student:
   def __init__(self, ID, name):
     self.ID = ID
     self.name = name
     self.score = 0

# ----- main -----
s1 = Student("6438027021", "Mark Zuckerberg")
s2 = Student("6438073821", "Lisa Blackpink")

"""#Part3: How to use object (access & update)

<font color=red>object</font><font color=blue>.property</font>

<font color=red>c</font><font color=blue>.radius</font><br>
<font color=red>c</font><font color=blue>.center</font>
"""

# Sample1: Point & Circle
# ----- class -----
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, p, r):
        self.center = p # Point
        self.radius = r

# ----- main -----
c = Circle( Point(2,30), 100 )

c.radius = 200
c.center = Point(2, 4)
c.center.x = 3

# Sample2: Book
# ----- class -----
class Book:
  def __init__(self, title, isbn, price):
    self.title = title
    self.isbn  = isbn
    self.price = price 

# ----- main -----
b1 = Book("Data Science", "149190142X", 28.79)

print( b1.title )

print( b1.price )
b1.price *= 0.80

print( b1.price )

# Sample2-1: add functions for Book
# ----- functions -----
def total_price( books ):
   s = 0
   for book in books:
       s += book.price
   return s

# ----- main -----
b1 = Book("Data Science",    "149190142X", 28.79)
b2 = Book("Learning Python", "1449355730", 37.06)
b3 = Book("Data Analysis",   "1449319793", 27.68)
books = [b1,b2,b3]
print( total_price( [b1, b2, b3] ) )

# Sample2-2: add functions for Book
# ----- functions -----
# no return value
def discount( books, p ):
  for b in books:
     b.price *= (1 - p/100)

# return a signle value (price)
def get_min_price( books ):
  return min([b.price for b in books])

# return object
def search( books, isbn ):
  for b in books:
    if isbn == b.isbn: 
      return b
  return None

for a in books :
  print(a.price)
discount(books,10)
for a in books :
  print(a.price)

"""##Exercise3: Student class (v3): calling properties

Create a function add_extra_score(student, extra) to Student. Call the function to add 20 points to s1.
"""

# ----- 1) class -----
class Student:

  def __init__(self,id,name,score) :
    self.id = id
    self.name = name
    self.score = 0

# ----- 2) function -----
def add_extra_score(s, extra):
  s.score += extra
  pass

# ----- 3) main -----
# s1 = Student("6438027021", "Mark Zuckerberg")
s1 = Student("6548083121","Paopao","")
add_extra_score(s1,20)
print(s1.score)
# add your code to add extra 20 points

#@title solution
# ----- 1) class -----
# https://pythontutor.com/
class Student:
   def __init__(self, ID, name):
     self.ID = ID
     self.name = name
     self.score = 0

# ----- 2) function -----
def add_extra_score(s, extra):
  s.score += extra

# ----- 3) main -----
s1 = Student("6438027021", "Mark Zuckerberg")
s2 = Student("6438073821", "Lisa Blackpink")

print(s1.score)
add_extra_score(s1, 20)
print(s1.score)

"""#Part4: Functions vs. Methods"""

#------------------------------------
# Part4-1) Class with no methods
# Methods outside class (not recommend)
#------------------------------------
# ----- 1) class -----
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# ----- 2) functions -----
def distance(p1, p2):
   dx = p1.x - p2.x
   dy = p1.y - p2.y
   return (dx**2+dy**2)**0.5

def to_str(p):
   return "(" + str(p.x) + \
          "," + str(p.y) + ")"

# ----- 3) main -----
p1 = Point(2,4)
p2 = Point(3,5)
d  = distance(p1, p2)
print( to_str(p1), to_str(p2) )

"""**Class contains two components:**


*   Properties (also called fields) - variables
*   Methods (also called actions) - functions


"""

#------------------------------------
# Part4-2) Class with methods
# Methods inside class (recommend)
#------------------------------------
# https://pythontutor.com/

# ----- 1) class -----
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self, p):
     dx = self.x - p.x
     dy = self.y - p.y
     return (dx**2+dy**2)**0.5

  def to_str(self):
   return "(" + str(self.x) + \
          "," + str(self.y) + ")"

# ----- 2) main -----
p1 = Point(2,4)
p2 = Point(3,5)

d  = p1.distance(p2) # call method
print( p1.to_str(), p2.to_str() ) # call method

#------------------------------------
# Part4-3) existing python class & methods
# Functions vs. Class Methods
#------------------------------------

# ----- Part1) just call functions -----
a = [1,2,3,4]
k = len(a)

print(a)
s = sum(a)
b = sorted(a)


# just call functions in other modules
import math
import numpy as np

k = math.sin(1)
d = np.ndarray((2,3))

# ----- Part2) call method from objects -----
# Actually, we have been using class/objects :)

# list is class.
a = [1,2,3,4]
a.sort()
a.append(99)

# string is class.
t = "aBc"
u = t.upper()
v = t.lower()
k = t.find("B")

# set is class.
s = set(a)
s = s.union([3,5])

#------------------------------------
# Part4-4) BankAccount class (v1)
# - There are 3 properties, 1 constructor, 2 methods
#------------------------------------

# ----- 1) class -----
class BankAccount:
    def __init__ (self, acc_no, acc_name, balance):
        self.acc_no   = acc_no
        self.acc_name = acc_name
        self.balance  = balance

    def deposit(self, amount):
        if amount > 0:
          self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
          self.balance -= amount

# ----- 2) main -----
a1 = BankAccount("1-034-567-892", "Mark Zuckerberg", 500)
a1.deposit(1000)
a1.withdraw(150)
print(a1.acc_no, a1.balance)

#------------------------------------
# Part4-4) BankAccount class (v2): call other methods
# - There are 3 properties, 1 constructor, 3 methods
# - adding transfer_to()
#------------------------------------

# ----- 1) class -----
class BankAccount:
    def __init__ (self, acc_no, acc_name, balance):
        self.acc_no   = acc_no
        self.acc_name = acc_name
        self.balance  = balance

    def deposit(self, amount):
        if amount > 0:
          self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
          self.balance -= amount

    def transfer_to(self, acc, amount):
        if 0 <= amount <= self.balance:
            self.withdraw( amount )
            acc.deposit( amount )

# ----- 2) main -----
a1 = BankAccount("1-034-567-892", "Mark Zuckerberg", 1000)
a2 = BankAccount("1-034-567-900", "Lisa Blackpink", 500)
print(a1.balance, a2.balance)
a1.transfer_to(a2, 200)
print(a1.balance, a2.balance)

#------------------------------------
# Part4-6) Rational class (class method vs object method)
# - gcd is called a private method. 
# - It can only be used within the class.
#------------------------------------

# ----- 1) class -----
class Rational:
    def __init__(self, n, d):
      g = Rational.gcd(n, d)
      self.n = n // g    # numerator   
      self.d = d // g   # denominator 

    def gcd(a, b):
      # stop when a can be divided by b
      while b != 0: 
        a, b = b, a%b
        print('a=',a, 'b=',b)
      return a

# ----- 2) main -----
r1 = Rational( 1, 2 )  # store 1/2
r2 = Rational( 4, 8 )  # store 1/2

print(r1.n, r1.d)
print(r2.n, r2.d)

print( Rational.gcd(6,9) )

"""##Exercise4: Student class (v4): adding method

Update Student class in Exercise3 to have the method add_extra_score(student, extra) inside the class.
"""

# ----- 1) class -----
class Student:
  def __init__(self, ID, name):
     self.ID = ID
     self.name = name
     self.score = 0

  def add_extra_score(self, extra):
    self.score += extra
  

# ----- 2) main -----
# s1 = Student("6438027021", "Mark Zuckerberg")

# add your code to add extra 20 points

#@title solution
# ----- 1) class -----
# https://pythontutor.com/
class Student:
  def __init__(self, ID, name):
     self.ID = ID
     self.name = name
     self.score = 0

  def add_extra_score(self, extra):
     self.score += extra

# ----- 2) main -----
s1 = Student("6438027021", "Mark Zuckerberg")
s2 = Student("6438073821", "Lisa Blackpink")

print(s1.score)
s1.add_extra_score(20)
print(s1.score)

"""#Part5: Magic Methods

## What are magic methods in Python?

**Magic methods** in Python are the special methods that start and end with *the double underscores*.
"""

#------------------------------------
# Rational class (v2) -- not preferred
#------------------------------------

# ----- 1) class -----
class Rational:
  def __init__(self, n, d):
    g = Rational.gcd(n, d)
    self.n = n // g    # numerator   
    self.d = d // g   # denominator 

  def gcd(a, b):
    # stop when a can be divided by b
    while b != 0: 
      a, b = b, a%b
    return a

  def mul(self, x):
    n = self.n * x.n
    d = self.d * x.d
    return Rational(n, d)

  def add(self, x):
    d = self.d * x.d
    n = self.n * x.d + x.n * self.d
    return Rational(n, d)

  def to_float(self):
    return self.n / self.d
  

  def less_than(self, x):
    return self.to_float() < x.to_float()
  

  def to_str(self):
    return str(self.n) + "/" + str(self.d)
    
  
# ----- 2) main -----
r1 = Rational(20,40)
r2 = Rational(1,4)

print(r1)
print(r1.to_str())
print()

r3 = r1.add(r2)
print(r3.to_str())
r4 = r1.mul(r2)
print(r4.to_str())
print(r3.less_than(r4))

#------------------------------------
# Rational class (v2) -- preferred
#------------------------------------

# ----- 1) class -----
class Rational:
  def __init__(self, n, d):
    g = Rational.gcd(n, d)
    self.n = n // g    # numerator   
    self.d = d // g   # denominator 

  def gcd(a, b):
    # stop when a can be divided by b
    while b != 0: 
      a, b = b, a%b
    return a

  def __mul__(self, x):
    n = self.n * x.n
    d = self.d * x.d
    return Rational(n, d)

  def __add__(self, x):
    d = self.d * x.d
    n = self.n * x.d + x.n * self.d
    return Rational(n, d)

  def __float__(self):
    return self.n / self.d
  

  def __lt__(self, x):
    return float(self) < float(x) 

  def __str__(self):
    return str(self.n) + "/" + str(self.d)
    
  
# ----- 2) main -----
r1 = Rational(20,40)
r2 = Rational(1,4)

print(r1)
print(str(r1))
print()

r3 = r1 + r2
print( str(r3), float(r3) )
r4 = r1 * r2
print( r3 < r4 )

"""## Item, menu, orders"""

# ----- 1) class -----
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# ----- 2) main -----
menu = [ Item("Fried rice",   45), 
         Item("Phat thai",    50),
         Item("Congee",       30),
         Item("Papaya salad", 40) ]

# ----- 1) class -----
class Order:
    def __init__(self):
        self.order_items = []
        self.paid = False

    def add(self, item, n):
        for i in range(n):
            self.order_items.append(item)

    def total(self):
        s = 0
        for item in self.order_items: 
            s += item.price
        return s

# ----- 2) main -----
o1 = Order(); 
o1.add(menu[0], 2); 
o1.add(menu[3], 1)

# ----- function -----
def get_total(orders):
  return sum( [od.total() for od in orders if od.paid] )

# ----- overall main -----
m = [ Item("Fried rice", 45),
      Item("Phat thai", 50),
      Item("Congee", 30), 
      Item("Papaya salad", 40) ]

o1 = Order()
o1.add(m[0],2); o1.add(m[3],1)
o2 = Order(); 
o2.add(m[0],1); o2.add(m[1],2)
o3 = Order(); 
o3.add(m[1],1); o3.add(m[2],1)
orders = [o1, o2, o3]

o1.paid = True
o2.paid = True
print(get_total(orders))

# ----- update Item class (v2) -----
class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def __lt__(self, rhs):
     return self.price < rhs.price

  def __str__(self):
     return self.name + ":" + str(self.price)

# ----- main -----
x1 = Item("Congee", 30)
x2 = Item("Phat thai", 50)
print(x1 < x2)          # True
print(x2 < x1)          # False
print(str(x1), str(x2)) # Congee:30, Phat thai:50
print(x1, x2)           # print

menu = [ Item("Fried rice",   45), 
         Item("Phat thai",    50),
         Item("Congee",       30), 
         Item("Papaya salad", 40) ]

menu.sort()
#menu.sort(reverse=True)

for item in menu:
    print(item)

"""##Date"""

# ----- 1) class -----
class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y
    def __lt__(self, rhs):
        d1 = (self.y, self.m, self.d)
        d2 = (rhs.y,  rhs.m,  rhs.d)
        return d1 < d2
    def __str__(self):
        return str(self.d) + "/" + \
               str(self.m) + "/" + \
               str(self.y)

# ----- 2) main -----
d1 = Date(20, 1, 1990)
d2 = Date(9, 12, 1990)
print( d1 < d2 )
print( d1, d2  )

"""![animation](https://c.tenor.com/rCfSLZ3YM_UAAAAC/cat-day-let-it-begin.gif)

"""

