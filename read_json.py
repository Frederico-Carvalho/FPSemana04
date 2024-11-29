import json

file = open ("data.json", "rt")
json_data = file.read()
data = json.loads(json_data)
print(data)

file.close()