point = {"particles": 10, "tikils": 90, "sick": 80}

point["particles"] = 89
name = dict([('particles', 838), ('pin', 73), ('like', 553)])
print(name)
print(point)
part = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

print(part['sape'])
if 'dam' in part:
    print(part['dam'])

del part['sape']
print(part)

for v in part.items():
    print(v)


# can use get("a", default_value)
