class Grandparent:
    def __init__(self):
        self._protected = 100
        self.__private = 200

    def _protected_function(self):
        print("Protected function")

    def __private_function(self):
        print("Private function")

    def show_private(self):
        print("Private variable:", self.__private)
        self.__private_function()


class Parent(Grandparent):
    def show_parent(self):
        print("Protected variable:", self._protected)
        self._protected_function()


class Child(Parent):
    def show_child(self):
        print("Child class")
        print("Protected variable:", self._protected)
        self._protected_function()


obj = Child()

obj.show_parent()
obj.show_child()
obj.show_private()