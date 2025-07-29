# Practical Example 1: How does the Python code structure work?

# Step 1: Define a function
def greet(name):
    print("Hello, " + name)

# Step 2: Main code
if __name__ == "__main__":
    your_name = input("Enter your name: ")  # Get input from user
    greet(your_name)  # Call the function
