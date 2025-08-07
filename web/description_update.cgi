#!/usr/bin/python3 

import psycopg2, cgi
import login
form = cgi.FieldStorage()
#getvalue uses the names from the form in previous page 
ean = form.getvalue('ean')
descr = form.getvalue('descr')

print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>Update Description</title>') 
print('</head>')
print('<body>') 
connection = None

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials) 
    cursor = connection.cursor()
    # Making query
    data = (ean, descr)
    sql = f"UPDATE product SET descr = '{descr}' WHERE ean = '{ean}';"
    cursor.execute(sql, data)
    if data == None:
        raise Exception('None exception, check your input')
    # The string has the {}, the variables inside format() will replace the {} 
    print('<h2>Query executed</h2>')
    print(f"<p>New description: {descr}</p><p>For product: {ean}</p>")
    # Commit the update (without this step the database will not change) 
    connection.commit()
    # Closing connection
    cursor.close() 
except Exception as e:
# Print errors on the webpage if they occur 
    print('<h1>An error occurred. :(</h1>') 
    print('<p>{}</p>'.format(e))
    print('<form action="http://web2.tecnico.ulisboa.pt/ist195493/homepage.cgi" method="post">')
    print('<input type="submit" value="Back to Homepage" />')
    print('</form>')
finally:
    if connection is not None:
        connection.close() 

print('<form action="http://web2.tecnico.ulisboa.pt/ist195493/homepage.cgi" method="post">')
print('<input type="submit" value="Back to Homepage" />')
print('</form>')
print('</body>')
