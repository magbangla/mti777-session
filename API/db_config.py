from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'magbangla'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'mti777'
app.config['MYSQL_DATABASE_HOST'] = 'db4free.net'
mysql.init_app(app)
