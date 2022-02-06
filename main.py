from flask import Flask, render_template
from posting import Posting
import requests

response = requests.get("https://api.npoint.io/8666554094e600d574a2")
posts = response.json()
post_obj_list = []

for x in posts:
    post_obj = (Posting(x["id"], x["body"], x["title"], x["subtitle"]))
    post_obj_list.append(post_obj)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=post_obj_list)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<int:id>')
def post(id):
    current_post = None
    for x in post_obj_list:
        if id == x.id:
            current_post = x
    return render_template("post.html", post=current_post)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="33")
