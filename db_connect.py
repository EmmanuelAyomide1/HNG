import MySQLdb
host = 'EmmyAyo.mysql.pythonanywhere-services.com'  # Replace with your MySQL host address
user = 'EmmyAyo'       # Replace with your MySQL username
password = '@guW!qqBrA3Lnxg'   # Replace with your MySQL password
database = 'EmmyAyo$default'   # Replace with the name of your MySQL database
connection = MySQLdb.connect(host=host, user=user, passwd=password, db=database)
cursor = connection.cursor()
cursor.close()
connection.close()
