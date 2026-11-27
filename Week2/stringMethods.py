text = "hello world"
print(text.capitalize())  # Output: "Hello world"
print(text.find("world"))  # Output: 6
print(text.find("world",0,5))  # Output: -1 because "world" is not in the substring from index 0 to 5
print(text.lower())  # Output: "hello world"
print(text.upper())  # Output: "HELLO WORLD"
print(text.startswith("world"))  # Output: False
print(text.startswith("world",6))  # Output: True because "world" starts at index 6
print(text.split())  # Output: ['hello', 'world']

text = "hello {name}, you are {age} years old."
print(text.format(name="Alice", age=25)) # Output: "hello Alice, you are 25 years old