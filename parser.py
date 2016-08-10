import random
from Item import Item



def genoutputs(items):
 	
	v = ''
	k = 0
	rows = ''
	for x in items:
		rows +=  x.ToHtmlRow();

	text = "<html>  <head>  <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">  <title>МСС-М</title>  </head> <body>  <table border=\"1\">   <caption>ИКСС</caption>   <tr>  <th>Пакет</th>    <th>Primary Packet Header</th>    <th>Идентификатор сегмента упакованных данных</th>   </tr>"\
	 + rows + '</body> </html>'
	return text

l= []
for x in range(1,10):
	i = Item()
	i.number = random.randint(1, 5)
	i.pheader = random.randint(1, 5)
	i.sigment = random.randint(1, 5)
	l.append(i)

#Выводит [Decode error - output not utf-8] Это ошибка сублайма.
#Решение тут https://toster.ru/q/158563

# Где запись в файл????

print(genoutputs(l))
#mtext = genoutputs()

#f = open('o.html', 'w', encoding='utf8')
#f.write(mtext)
#f.close()