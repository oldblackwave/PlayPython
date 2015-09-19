import json

s = json.loads('{"name":"test","type":"TT"}')
print(s)
print(s.keys())
print(s["name"])
print(s["type"])