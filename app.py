from flask import Flask
app = Flask(__name__)
import psycopg2

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://rtolandlab10_db_user:I9LVBtBre4ZwtoIPFXQLH5kMpn0ODD6R@dpg-cl5dpmd6fh7c73elllig-a/rtolandlab10_db")
    conn.close()
    return "Database Connection Successful"
