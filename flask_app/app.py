from flask import Flask, render_template
import psycopg2
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():

    conn = psycopg2.connect(host= os.getenv("HOST"),
                            dbname= os.getenv("DBNAME"),
                            user =  os.getenv("USER"),
                            password = os.getenv("PASSWORD"),
                            port =os.getenv("PORT"))
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT title, image_url FROM items")
        items = cur.fetchall()

    return render_template('index.html', items=items)

if __name__ == '__main__':
    data = {
        "host": os.getenv("HOST"),
        "dbname": os.getenv("DBNAME"),
        "user": os.getenv("USER"),
        "password": os.getenv("PASSWORD"),
        "port": os.getenv("PORT")
    }
    print(data)
    app.run(host='0.0.0.0', port=8080, debug=True)