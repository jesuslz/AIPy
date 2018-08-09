import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '127.0.0.1' 
database = '/Users/mirnazertuche/Desktop/tutorial.db' 
username = 'mirnazertuche' 
password = 'AdrianValdes2922' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()