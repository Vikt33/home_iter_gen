import hashlib

def MyCenerator(path):
    with open(path, encoding='utf-8') as file:
        for line in file:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()

for i in MyCenerator('test.txt'):
    print(i)
