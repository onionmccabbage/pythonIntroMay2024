# the JSON format is very popular for data transfer and storage
# JavaScript Object Notation - it is NOT JAVASCRIPT it is TEXT
# Python has tools to work with JSON
import json
# here is a complex list of dictionaries with child lists etc.
my_l = [
  {
    "name": "Molecule Man",
    "age": 29,
    "secretIdentity": "Dan Jukes",
    "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
  },
  {
    "name": "Madame Uppercut",
    "age": 39,
    "secretIdentity": "Jane Wilson",
    "powers": [
      "Million tonne punch",
      "Damage resistance",
      "Superhuman reflexes"
    ]
  }
]

my_j = json.dumps(my_l) # converts a structure to JSON
print(my_j, type(my_j))
my_l = json.loads(my_j) # convert JSON into a structure
print(my_l[1]['powers'][2]) # "Superhuman reflexes"