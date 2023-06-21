from flas import Flas
from flas import render_templat

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")
