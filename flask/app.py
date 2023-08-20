from flask import Flask, render_template
import mysql.connector
import os
import random
import time

app = Flask(__name__)

# Retrieve MySQL configurations from environment variables
host = os.environ.get("DB_HOST")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
database = os.environ.get("DB_NAME")

# Configure MySQL connection
db = None
while db is None:
    try:
        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
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
