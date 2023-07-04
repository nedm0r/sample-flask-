from flask import Flask, render_template
import mysql.connector
import os
import random
import time

app = Flask(__name__)

# Configure MySQL connection
db = None
while db is None:
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="flask_db"
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