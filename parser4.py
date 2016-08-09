import random

class Item():
	def __init__(self):
		pass

	def ToHtmlRow(self):
		q = ''
		for x in l:
			a = ''
			for prop in x.__dict__.keys():
				#print("{0}".format(getattr(x, prop)))
				q = getattr(x, prop)
				print ("q = ", q)
				o = str (q)
				a = a  + o
			print ('a =', a)	
			s = tuple(a)
			q = "<tr><td> {} </td><td> {} </td><td> {} </td></tr>".format(*s)
			print (q)
			print(type(q))	
			print("-----")
			pass

l= []
for x in range(1,10):
	i = Item()
	i.number = random.randint(1, 5)
	i.pheader = random.randint(1, 5)
	i.sigment = random.randint(1, 5)
	l.append(i)

i.ToHtmlRow()