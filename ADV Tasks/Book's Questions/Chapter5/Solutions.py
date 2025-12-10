# ==================================================
# 1- Rectangle Class:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}") 

# ==================================================
# 2- Employee Class with Alternative Constructor:

class Employee:
    def __init__(self,name,employee_id,salary):
        self.name=name
        self.employee_id=employee_id
        self.salary=salary

    @classmethod
    def from_string(cls,employee_str):
        name, emp_id, salary = employee_str.split(',')
        return cls(name, emp_id, float(salary))
    
    def display_info(self):
        print(self.name)
        print(self.employee_id)
        print(self.salary)

e1 = Employee.from_string("John Doe, E123, 50000")
e2 = Employee('Badry', 'A123', 80000)
e1.display_info()
e2.display_info()

# ==================================================
# 3- Vehicle Hierarchy:

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

class Bike(Vehicle):
    def move(self):
        print("Bike is cycling")

vehicles = [Vehicle(), Car(), Bike()]
for vehicle in vehicles:
    vehicle.move()

# ==================================================
# 4- Vector Class with Operator Overloading:

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __sub__(self,other):
        return Vector(self.x-other.x , self.y-other.y)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
vector1 = Vector(5,6)
vector2 = Vector(2,3)
print(f"Sub = {vector1 - vector2}")
print(f"multiple = {vector1*vector2}")

# ==================================================
# 5- Shape Polymorphism Function:

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius*self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height
    
    def area(self):
        return self.width*self.height

def print_shape_area(shape):
    print(f"area= {shape.area()}")
shapes = [Shape(), Circle(5), Rectangle(4, 6)]
for i in shapes:
    print_shape_area(i)