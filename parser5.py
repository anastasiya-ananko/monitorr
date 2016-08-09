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
			#print("-----")
			return q


def genoutputs():
 	
	v = ''
	k = 0
	while k < 4:
		q = i.ToHtmlRow()
		print (q)
		k = k + 1
		v = v + q
	print (v)	
	text = '<html>  <head>  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">  <title>МСС-М</title>  </head> <body>  <table border="1">   <caption>ИКСС</caption>   <tr>  <th>Пакет</th>    <th>Primary Packet Header</th>    <th>Идентификатор сегмента упакованных данных</th>   </tr>' + v + '</body> </html>'
	print(text)
	return text

l= []
for x in range(1,10):
	i = Item()
	i.number = random.randint(1, 5)
	i.pheader = random.randint(1, 5)
	i.sigment = random.randint(1, 5)
	l.append(i)

i.ToHtmlRow()
#mtext = genoutputs()

#f = open('o.html', 'w', encoding='utf8')
#f.write(mtext)
#f.close()