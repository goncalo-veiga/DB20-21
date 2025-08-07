#!/usr/bin/python3 
import cgi
form = cgi.FieldStorage()
print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>Data Base HTML Manager</title>') 
print('</head>')
print('<body>')

print('<h3>Insert category name</h3>')
print('<form action="category_update.cgi" method="post">')
print('<p>Category name: <input type="text" name="name" required/></p>') 
print('<p><input type="submit" value="Create Category"/></p>')
print('</form>')

print('<h3>Insert Sub Categories</h3>')
print('<form action="http://web2.tecnico.ulisboa.pt/ist195493/sub_category.cgi" method="post">')
print('<input type="submit" value="Go to Categories" />')
print('</form>')

print('<h3>Remove category</h3>')
print('<form action="remove_category_update.cgi" method="post">')
print('<p>Category name: <input type="text" name="name" required/></p>') 
print('<p><input type="submit" value="Remove Category"/></p>')
print('</form>')

print('<h3>Insert product</h3>')
print('<form action="insert_product.cgi" method="post">')
print('<p>Product ean: <input type="text" name="ean" required/></p>')
print('<p>Product description: <input type="text" name="descr" required/></p>')
print('<p>Product category: <input type="text" name="category" required/></p>')
print('<p>Primary Supplier nif: <input type="text" name="p_nif" required/></p>')
print('<p>Primary supplied since: <input type="date" name="date" required/></p>')
print('<p>Secondary Supplier nif: <input type="text" name="s1_nif" required/></p>')
print('<p>Secondary Supplier nif (optional): <input type="text" name="s2_nif"/></p>')
print('<p>Secondary Supplier nif (optional): <input type="text" name="s3_nif"/></p>')
print('<p><input type="submit" value="Create product"/></p>')
print('</form>')

print('<h3>Remove product</h3>')
print('<form action="remove_product.cgi" method="post">')
print('<p>Product ean: <input type="text" name="ean" required/></p>')
print('<p><input type="submit" value="Remove Product"/></p>')
print('</form>')


print('<h3>List replenish event</h3>')
print('<form action="replenish_event.cgi" method="post">')
print('<p>Product ean: <input type="text" name="ean" required/></p>') 
print('<p><input type="submit" value="List"/></p>')
print('</form>')

print('<h3>Change product description</h3>')
print('<form action="description.cgi" method="post">')
print('<p>Product ean: <input type="text" name="ean" required/></p>') 
print('<p><input type="submit" value="Change"/></p>')
print('</form>')

print('<h3>List all sub categories</h3>')
print('<form action="list_categories.cgi" method="post">')
print('<p>Super category: <input type="text" name="super" required/></p>') 
print('<p><input type="submit" value="List"/></p>')
print('</form>')


print('</body>') 
print('</html>')