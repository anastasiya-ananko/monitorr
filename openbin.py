import os
import msvcrt

path = 'demo data/Route1.vld'
# size = os.path.getsize(path)
size = 8000

print(size)

f = open(path, 'rb+')

PACKET_SIZE = 4096;
offset = 0

print("start")

while offset < size:
	a = f.read(8)
	row = "{0:02x} {1:02x} {2:02x} {3:02x} | {4:02x} {5:02x} {6:02x} {7:02x}".format(*a)

	# for x in a:
	# 	row = row + ' ' + format(x, '02x')

	print(row.upper())
	f.seek(offset)
	offset = offset + PACKET_SIZE

print("end")

msvcrt.getch()