from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")


@app.route("/")
def index():
    listings = mongo.db.listings.find_one()
    return render_template("index.html", listings=listings)


@app.route("/scrape")
def scraper():
    mars_db = mongo.db.mars_db
    mars_data = scrape_mars.scrape()
    mars_db.update({}, mars_data)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
