from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
	class Book(db.Model):
		id = db.Column(db.Integer, primary_key=True)
		title = db.Column(db.String(250), unique=True, nullable=False)
		author = db.Column(db.String(250), nullable=False)
		rating = db.Column(db.Float, nullable=False)
	
		def __repr__(self):
			return "<Book %r" % self.title
	
	
	db.create_all()
	
	
	new_book = Book(id=1, title="Redwall", author="Brian Jacques", rating=8.7)
	db.session.add(new_book)
	db.session.commit()

# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# # cursor.execute(
# # 	"CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, "
# # 	"rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Redwall', 'Brian Jacques', '8.7')")
# db.commit()
