#!/usr/bin/python3 

import psycopg2, cgi
import login
form = cgi.FieldStorage()
#getvalue uses the names from the form in previous page 
category_name = form.getvalue('category_name')
sub_category_name = form.getvalue('sub_category_name')

print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>Category</title>') 
print('</head>')
print('<body>') 
connection = None

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials) 
    cursor = connection.cursor()
    # Making query
    data = (category_name, sub_category_name)
    sql1 = f"INSERT INTO category values ('{sub_category_name}');"
    cursor.execute(sql1, data[1])
    sql2 = f"INSERT INTO simple_category values ('{sub_category_name}');"
    cursor.execute(sql2, data[1])
    sql3 = f"INSERT INTO consists_of values ('{category_name}', '{sub_category_name}');"
    cursor.execute(sql3, data)
    
    if data == None:
        raise Exception('None exception, check your input')
    # The string has the {}, the variables inside format() will replace the {} 
    print('<h2>Query executed</h2>')
    print(f"<p>'{data}' created</p>")
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
