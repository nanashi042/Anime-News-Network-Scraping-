from flask import Flask , render_template
from package import scraper

app = Flask(__name__)

@app.route('/')
def home():
    lst = scraper.get_image()
    ttl = scraper.get_name()
    return render_template("index.html", lst = lst , title=ttl)

@app.route('/single-post')
def single_post():
    return render_template("single-post.html")

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
