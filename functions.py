# print is a function
print("Hello")

#length function
my_length = len("hello")
print(my_length)

#defining a function
def my_function():
    print("it is a function")

#calling a function
my_function()   

#Functions with inputs
def greet(name):
    print(f"Hello {name}!")
   
greet("Peter Parker")  


def greet_with(name, location):
    print(f"Hi {name}!")
    print(f"What is the weather in {location}?")

greet_with("Bruce Wayne", "Gotham")
