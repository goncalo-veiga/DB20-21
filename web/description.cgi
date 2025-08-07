#!/usr/bin/python3 
import cgi
form = cgi.FieldStorage()

ean = form.getvalue('ean')

print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>Description Update</title>') 
print('</head>')
print('<body>')


print(f'<h3>Change description for product {ean}</h3>')
print('<form action="description_update.cgi" method="post">')
print(f'<p><input type="hidden" name="ean" value="{ean}"/></p>')
print('<p>New description: <input type="text" name="descr"/></p>') 
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')

print('</body>') 
print('</html>')