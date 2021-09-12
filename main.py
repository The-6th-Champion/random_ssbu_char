from flask import Flask, render_template, request
from rdoclient import RandomOrgClient
from fighters import fighters
from generate import get_random, get_fighter
import os

app = Flask(__name__)
fighter_list = []
r = RandomOrgClient(os.getenv("API_KEY"))

@app.route("/", methods = ["GET", "POST"])
def hello_world():    
    if request.method == "POST":
        num = request.form['num']
        for i in get_fighter(get_random(num, r)):
            fighter_list.append(i)
        return render_template("index.html", flist = fighter_list)
    return render_template("index.html", flist = fighter_list)


if __name__ == "__main__":
    app.run()