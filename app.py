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

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://rtolandlab10_db_user:I9LVBtBre4ZwtoIPFXQLH5kMpn0ODD6R@dpg-cl5dpmd6fh7c73elllig-a/rtolandlab10_db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('db_insert')
def inserting():
    conn = psycopg2.connect("postgres://rtolandlab10_db_user:I9LVBtBre4ZwtoIPFXQLH5kMpn0ODD6R@dpg-cl5dpmd6fh7c73elllig-a/rtolandlab10_db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball(First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"
