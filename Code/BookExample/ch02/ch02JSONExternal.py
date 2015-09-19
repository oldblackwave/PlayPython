import json

orig = '''{"name":"test","type":"TT"}
        {"name":"test","type":"TT"}
        {"name":"test","type":"TT"}
        {"name":"test","type":"TT"}'''
        
s = json.loads('{"name":"test","type":"TT"}')
print(s)
print(s.keys())
print(s["name"])
print(s["type"])

print('\n')

for line in orig.split('\n'):
    orig_doc = json.loads(line)
    print(orig_doc)
