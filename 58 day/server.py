from flask import Flask, render_template
import random
import datetime
import requests

apikey = "71b0d3cd53d50d6f95a68312f3bf0def"
app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    # Pass the random number to the template
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess_game/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    url = f"https://api.agify.io?name={name}"
    age_response = requests.get(url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", person_name=name, gender=gender, age=age)

@app.route("/blog")
def blog():
    blog_url = ""

if __name__ == "__main__":
    app.run(debug=True)
