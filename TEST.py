filepath1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": 2
}
filepath2 = {
    "timeout": 20,
    "verbose": 3,
    "host": "hexlet.io"
}

print('{')
for i in sorted(filepath1.items()):
    if i in filepath2.items():
        print(' ', *i)
    elif i not in filepath2.items():
        print(' -', *i)

for j in sorted(filepath2.items()):
    if j not in filepath1.items():
        print(' +', *j)
print('}')
