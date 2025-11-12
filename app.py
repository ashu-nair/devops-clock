from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/time")
def get_time():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return {"time": now}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
