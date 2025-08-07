#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()
ean = form.getvalue('ean')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Remove Product</title>')
print('</head>')
print('<body>')

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials) 
    cursor = connection.cursor()
    # Making query

    remove_secs = f"DELETE FROM supplies_sec WHERE ean = '{ean}';"
    cursor.execute(remove_secs, ean)

    remove_prim = f"DELETE FROM supplies_prim WHERE ean = '{ean}';"
    cursor.execute(remove_prim, ean)

    remove_prod = f"DELETE FROM product WHERE ean = '{ean}';"
    cursor.execute(remove_prod, ean)

    # The string has the {}, the variables inside format() will replace the {} 
    # Commit the update (without this step the database will not change) 
    connection.commit()
    # Closing connection
    cursor.close()

    print('<p>Product removed or doesnt exist</p>')

except Exception as e:
# Print errors on the webpage if they occur 
    print('<h1>An error occurred. :(</h1>') 
    print('<p>{}</p>'.format(e))
finally:
    if connection is not None:
        connection.close() 

print('</body>')
print('</html>')
