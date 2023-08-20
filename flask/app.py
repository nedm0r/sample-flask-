from flask import Flask, render_template
import mysql.connector
import os
import random
import time

app = Flask(__name__)


# Retrieve MySQL configurations from environment variables
db_host = os.environ.get("MYSQL_HOST", "db")
db_user = os.environ.get("MYSQL_USER", "root")
db_password = os.environ.get("MYSQL_PASSWORD")
db_database = os.environ.get("MYSQL_DATABASE", "flask_db")

# Configure MySQL connection
db = None
while db is None:
    try:
       db = mysql.connector.connect(
       host=db_host,
       user=db_user,
       password=db_password,
       database=db_database
    )
 
    except mysql.connector.Error as err:
        print("Failed connecting to database. Retrying...")
        time.sleep(1)

@app.route("/")
def index():
    cursor = db.cursor()
    cursor.execute("SELECT url FROM images;")
    images = [row[0] for row in cursor.fetchall()]
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
