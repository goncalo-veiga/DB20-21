#!/usr/bin/python3 
import psycopg2
import login
print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>Super Categories</title>') 
print('</head>')
print('<body>') 
print('<h3>Categories</h3>')
connection = None 

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials) 
    cursor = connection.cursor()

    # Making query
    sql = 'SELECT category_name FROM super_category;' 
    cursor.execute(sql)
    result = cursor.fetchall()
    num = len(result)

    # Displaying results
    print('<table border="0" cellspacing="5">') 
    for row in result:
        print('<tr>')
        for value in row:
        # The string has the {}, the variables inside format() will replace the
            print('<td>{}</td>'.format(value))
        print('<td><a href="insert_sub_category.cgi?category_name={}">Insert sub-category</a></td>'.format(row[0])) 
        print('</tr>')
    
    print('</table>')
    # Closing connection
    cursor.close() 
except Exception as e:
    # Print errors on the webpage if they occur 
    print('<h1>An error occurred.</h1>') 
    print('<p>{}</p>'.format(e))
finally:
    if connection is not None:
        connection.close()
print('</body>') 
print('</html>')