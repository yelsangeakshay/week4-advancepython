import json

lst = [1,2,3,4,5]
d= {"name":"Akshay",
    "age":10}
with open("demo.json",'w') as f:
    json.dump(d,f)

with open("demo.json",'r') as f:
    print(json.load(f))