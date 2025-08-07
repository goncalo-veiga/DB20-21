#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()
ean = form.getvalue('ean')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Replenish Event</title>')
print('</head>')
print('<body>')


try:
	# Creating connection
	connection = psycopg2.connect(login.credentials)
	cursor = connection.cursor()

	# Making query
	sql = f"SELECT * FROM replenish_event WHERE ean = '{ean}';"
	cursor.execute(sql)
	result = cursor.fetchall()

	print('<table border="5">')
	print('<tr><td>ean</td><td>nif</td><td>nr</td><td>side</td><td>height</td><td>instant</td><td>units</td></tr>')
	for row in result:
		print('<tr>')
		print('<td>', row[0], '</td><td>', row[1], '</td><td>', row[2], '</td><td>', row[3], '</td><td>', row[4], '</td><td>', row[5], '</td><td>', row[6], '</td>')
		print('</tr>')
	print('</table>')

	#Closing connection
	cursor.close()
	connection.close()
except Exception as e:
	print('<h1>An error occurred.</h1>')
	print('<p>', e, '</p>')
        print('<form action="http://web2.tecnico.ulisboa.pt/ist195493/homepage.cgi" method="post">')
        print('<input type="submit" value="Back to Homepage" />')
        print('</form>')

print('<form action="http://web2.tecnico.ulisboa.pt/ist195493/homepage.cgi" method="post">')
print('<input type="submit" value="Back to Homepage" />')
print('</form>')

print('</body>')
print('</html>')
