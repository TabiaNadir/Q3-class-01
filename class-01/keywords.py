# if/else: Making decisions
temperature = 35
if temperature > 30:
    print("It's hot outside!")
else:
    print("Nice weather!")

# for: Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# def: Define a function
def greet(name):
    return f"Hello, {name}!"

print(greet("Tabia"))

# class: Define a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(f"My car is a {my_car.brand} {my_car.model}")

# try/except: Handle errors
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# with/as: File handling
# with open("data.txt", "r") as file:
#     content = file.read()

# lambda: Short function
double = lambda x: x * 2
print(double(5))

# global/nonlocal: Scope control
count = 0

def increase():
    global count
    count += 1

increase()
print(count)
