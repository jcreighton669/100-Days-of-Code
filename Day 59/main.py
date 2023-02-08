from flask import Flask, render_template
import requests

app = Flask(__name__)
URL = "https://api.npoint.io/e9d7761bde7444819f4d"
posts = requests.get(URL).json()


@app.route('/')
def home():
	return render_template("index.html", all_posts=posts)


@app.route('/post/<int:index>')
def show_post(index):
	requested_post = None
	for blog_post in posts:
		if blog_post["id"] == index:
			requested_post = blog_post
	return render_template("post.html", post=requested_post)


@app.route('/about')
def show_about():
	return render_template("about.html")


@app.route('/contact')
def show_contact():
	return render_template("contact.html")


if __name__ == "__main__":
	app.run(debug=True)
