#!/usr/bin/python3 
import cgi
form = cgi.FieldStorage()

category_name = form.getvalue('category_name')

print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>Insert Sub Category</title>') 
print('</head>')
print('<body>')

# The string has the {}, the variables inside format() will replace the {} 
print(f'<h3>Insert sub category name for Super Category {category_name}</h3>')

# The form will send the info needed for the SQL query 
print('<form action="sub_category_update.cgi" method="post">')
print('<p><input type="hidden" name="category_name" value="{}"/></p>'.format(category_name))
print('<p>Sub Category name: <input type="text" name="sub_category_name"/></p>')
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')

print('</body>') 
print('</html>')