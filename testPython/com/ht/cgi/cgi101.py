#!C:/Users/Administrator/AppData/Local/Programs/Python/Python36/python.exe  
  
import cgi  
import cgitb  
  
form = cgi.FieldStorage() # parse form data  
username=form.getvalue('user');
print('Content-Type:text/html\n') # hdr plus blank line  
print()  
print('<title>Reply Page</title>') # html reply page  
print('<a href="javaScript:void(0)">%s</a>'%username);
if not 'user' in form:  
    print('<h1>Who are you?</h1>')  
else:  
    print('<h1>Hello <i>%s</i>!</h1>' % cgi.escape(form['user'].value)) 