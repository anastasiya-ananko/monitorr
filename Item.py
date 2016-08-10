import random

class Item():
	def __init__(self):
		pass

	def ToHtmlRow(self):
		values = ''
		for prop in self.__dict__.keys():
			#print("{0}".format(getattr(x, prop)))
			attr = getattr(self, prop)
			val = str (attr)
			values = values + val + ',' 
		return "<tr><td> {} </td><td> {} </td><td> {} </td></tr>".format(*(values.split(',')))

if __name__ == '__main__':
	l= []
	for x in range(1,10):
		i = Item()
		i.number = random.randint(1, 5)
		i.pheader = random.randint(1, 5)
		i.sigment = random.randint(1, 5)
		l.append(i)

	for x in l:
		print(x.ToHtmlRow())