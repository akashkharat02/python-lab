class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

obj = B()
obj.show_a()
obj.show_b()


class Father:
    def father(self):
        print("Father class")

class Mother:
    def mother(self):
        print("Mother class")

class Child(Father, Mother):
    def child(self):
        print("Child class")

obj = Child()
obj.father()
obj.mother()
obj.child()


class Grandparent:
    def grandparent(self):
        print("Grandparent class")

class Parent(Grandparent):
    def parent(self):
        print("Parent class")

class Child(Parent):
    def child(self):
        print("Child class")

obj = Child()
obj.grandparent()
obj.parent()
obj.child()


class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()

class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C(A):
    def show_c(self):
        print("Class C")

class D(B, C):
    def show_d(self):
        print("Class D")

obj = D()
obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()