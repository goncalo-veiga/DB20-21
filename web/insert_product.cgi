#!/usr/bin/python3
import cgi
import psycopg2
import login

form = cgi.FieldStorage()
ean = form.getvalue('ean')
descr = form.getvalue('descr')
category = form.getvalue('category')
p_nif = form.getvalue('p_nif')
date = form.getvalue('date')
s1_nif = form.getvalue('s1_nif')
s2_nif = form.getvalue('s2_nif')
s3_nif = form.getvalue('s3_nif')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Create Product</title>')
print('</head>')
print('<body>')

try:
    # Creating connection
    connection = psycopg2.connect(login.credentials) 
    cursor = connection.cursor()
    # Making query
    data = (ean, descr, category, p_nif, s1_nif, s2_nif, s3_nif)

    check_category = f"SELECT name FROM category WHERE name = '{category}';"
    cursor.execute(check_category, category)
    result = cursor.fetchall()
    if result == None:
        raise Exception(f'Category "{category}" does not exist')
    
    check_p_nif = f"SELECT nif FROM supplier WHERE nif = '{p_nif}';"
    cursor.execute(check_p_nif, p_nif)
    result = cursor.fetchall()
    if result == None:
        raise Exception(f'Supplier "{p_nif}" does not exists')

    check_s1_nif = f"SELECT nif FROM supplier WHERE nif = '{s1_nif}';"
    cursor.execute(check_s1_nif, s1_nif)
    result = cursor.fetchall()
    if result == None:
        raise Exception(f'Supplier "{s1_nif}" does not exists')

    if (s2_nif != None and s3_nif == None):
        check_s2_nif = f"SELECT nif FROM supplier WHERE nif = '{s2_nif}';"
        cursor.execute(check_s2_nif, s2_nif)
        result = cursor.fetchall()
        if result == None:
            raise Exception(f'Supplier "{s2_nif}" does not exists')

    if (s3_nif != None and s2_nif == None):
        check_s3_nif = f"SELECT nif FROM supplier WHERE nif = '{s3_nif}';"
        cursor.execute(check_s3_nif, s3_nif)
        result = cursor.fetchall()
        if result == None:
            raise Exception(f'Supplier "{s3_nif}" does not exists')

    if (s2_nif != None and s3_nif != None):
        check_s2_nif = f"SELECT nif FROM supplier WHERE nif = '{s2_nif}';"
        cursor.execute(check_s2_nif, s2_nif)
        result = cursor.fetchall()
        if result == None:
            raise Exception(f'Supplier "{s2_nif}" does not exists')

        check_s3_nif = f"SELECT nif FROM supplier WHERE nif = '{s3_nif}';"
        cursor.execute(check_s3_nif, s3_nif)
        result = cursor.fetchall()
        if result == None:
            raise Exception(f'Supplier "{s3_nif}" does not exists')
        
    check_date = f"SELECT '{date}' < CURRENT_DATE;"
    cursor.execute(check_date)
    result = cursor.fetchall()
    if result == 'f':
        raise Exception(f'Date {date} invalid')

    sql = f"INSERT INTO product values ('{ean}', '{descr}', '{category}');"
    cursor.execute(sql, (ean, descr, category))
    
    p_query = f"INSERT INTO supplies_prim values ('{p_nif}', '{ean}', '{date}');"
    cursor.execute(p_query, (p_nif, ean, date))
 
    s1_query = f"INSERT INTO supplies_sec values ('{s1_nif}', '{ean}');"
    cursor.execute(s1_query, (s1_nif, ean))

    if s2_nif != None:
        s2_query = f"INSERT INTO supplies_sec values ('{s2_nif}', '{ean}');"
        cursor.execute(s2_query, (s2_nif, ean))

    if s3_nif != None:
        s3_query = f"INSERT INTO supplies_sec values ('{s3_nif}', '{ean}');"
        cursor.execute(s3_query, (s3_nif, ean))

    print('<p>Queries executed</p>')
    # The string has the {}, the variables inside format() will replace the {} 
    # Commit the update (without this step the database will not change) 
    connection.commit()
    # Closing connection
    cursor.close() 
except Exception as e:
# Print errors on the webpage if they occur 
    print('<h1>An error occurred. :(</h1>') 
    print('<p>{}</p>'.format(e))
finally:
    if connection is not None:
        connection.close() 

print('</body>')
print('</html>')
