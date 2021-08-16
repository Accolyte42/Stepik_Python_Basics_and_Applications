import json

student1 = {
    "first_name": "Greg",
    "last_name": "Dean",
    "certificate": True,
    "scores": [70, 80, 90],
    "description": "Good job, Greg"
}

student2 = {
    "first_name": "Wirt",
    "last_name": "Wood",
    "certificate": True,
    "scores": [80.2, 80, 80],
    "description": "GJ"
}

data = [student1, student2]
print(json.dumps(data, indent=4, sort_keys=True)) # вывод внизу
with open('students.json', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)
# js = json.loads(input())
