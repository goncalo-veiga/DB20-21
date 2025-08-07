#!/usr/bin/python3 

import psycopg2, cgi
import login
form = cgi.FieldStorage()
#getvalue uses the names from the form in previous page 
super_name = form.getvalue('super')

print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>List Sub Categories</title>') 
print('</head>')
print('<body>') 
connection = None

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials) 
    cursor = connection.cursor()
    # Making query
    data = (super_name)
    sql = f"SELECT sub_name FROM consists_of WHERE super_name = '{data}';"
    if data == None:
        raise Exception('None exception, check your input')
    cursor.execute(sql, data)
    result = cursor.fetchall()
    
    print('<table border="5">')
    print('<tr><td>sub_category</td></tr>')

    for row in result:
        print('<tr>')
        print(f"<td>{row[0]}</td>")
        print('</tr>')
    print('</table>')
    # The string has the {}, the variables inside format() will replace the {} 
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
print('</html>')
