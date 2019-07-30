#!/usr/bin/python  # Will use this Environment Path for Python version

# Here is an example of constructing strings
var = 'Hello World'
var1 = "Hello World with Double Quotes"

# Here is How to Print a Variable
print(var)
print(var1)

# Here we will combine the string
stringCombo = (var + ' ' + var1)
print(stringCombo)

# Open JSON file as object with read() method
with open('auth.json') as config_file:
  data = json.load(config_file) 
  username = data['value1']
  password = data['value2']

# Open JSON file as string
with open('auth.json') as config_file:
  data = json.loads(config_file.read())
  username = data['value1']
  password = data['value2']
    
