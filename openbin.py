import os

path = 'Route1.vld'
size = os.path.getsize(path)
print(size)

f = open('Route1.vld', 'rb+')
n = 4096

while n < size:
	a = f.read(6)
	print(a)
	f.seek(n)
	n = n + 4096
