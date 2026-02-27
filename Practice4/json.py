import json

data = {
    "name": "Miras",
    "age": 16,
    "languages": ["Kazakh", "Russian", "English"],
    "active": True
}

json_text = json.dumps(data, indent=2, ensure_ascii=False)#dumps-it converts a Python object → JSON text (a string)
print(json_text)







import json
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)#load-read JSON and convert it into Python objects
print(y["age"])




import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) #{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
