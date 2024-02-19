file1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": "false"
}

file2 = {
  "timeout": 20,
  "verbose": "true",
  "host": "hexlet.io"
}

print('{')
for i in sorted(file1.items()):
    if i in file2.items():
        print(' ', *i)
    elif i not in file2.items():
        print(' -', *i)

for j in sorted(file2.items()):
    if j not in file1.items():
        print(' +', *j)
print('}')
