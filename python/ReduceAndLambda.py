# Import reduce from functools
from functools import reduce


# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda a,b:a+b, stark)

# Print the result
print(result)