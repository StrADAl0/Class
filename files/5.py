a = input()
with open(a, 'rb') as b, open('output.dat.', 'wb') as c:
    for elem in b.read().decode().split('\n'):
        c.write(bytes(elem[::-1] + '\n', 'UTF-8'))