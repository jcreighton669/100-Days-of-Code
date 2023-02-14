from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
URL = "https://api.npoint.io/e9d7761bde7444819f4d"
MY_EMAIL = "jacreighton669@gmail.com"
MY_PASSWORD = "hwaegdrycxwfmmyv"
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


@app.route('/contact', methods=["GET", "POST"])
def contact():
	if request.method == "POST":
		data = request.form
		send_email(data["name"], data["email"], data["phone"], data["message"],)
		return render_template("contact.html", msg_sent=True)
	return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
	email_message = f"Subject:NewMessage\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
	with smtplib.SMTP("smtp.gmail.com") as connect:
		connect.starttls()
		connect.login(MY_EMAIL, MY_PASSWORD)
		connect.sendmail(MY_EMAIL, MY_EMAIL, email_message)

if __name__ == "__main__":
	app.run(debug=True)
