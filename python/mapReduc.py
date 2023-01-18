value="ram"
def map(key, value):
  # process key-value pair and output intermediate key-value pairs
  for word in value.split():
    emit(word, 1)

def reduce(key, values):
  # sum up the values for each key and output final key-value pairs
  total = 0
  for value in values:
    total += value
  emit(key, total)
def emit(key, value):
  print(key, value)