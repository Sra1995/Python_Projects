import json

# a Python object (dict):
x = {
  "name": "Chuck Norris",
  "age": 82,
  "city": "Ryan",
  "State": "Oklahoma"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
