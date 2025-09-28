# Basic print statement
print("Hello")

# Using len() to get string length
text_length = len("hello")
print(f"Length of 'hello': {text_length}")

# Defining a simple function
def print_message():
    """Prints a simple message."""
    print("This is a function")

# Calling the function
print_message()

# Function with a single input parameter
def greet(name):
    """Greets a person by name."""
    print(f"Hello, {name}!")

# Calling the greet function
greet("Peter Parker")

# Function with multiple input parameters
def greet_with_location(name, location):
    """Greets a person and asks about the weather in their location."""
    print(f"Hi, {name}!")
    print(f"What is the weather like in {location}?")

# Calling the function with multiple parameters
greet_with_location("Bruce Wayne", "Gotham")