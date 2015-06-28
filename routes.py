from flask import Flask, render_template, url_for, g
import sqlite3

app = Flask(__name__)

app.database = "familjen.db"


def connect_db():
	return sqlite3.connect(app.database)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/members')
def members():
	g.db = connect_db()
	cur = g.db.execute('select * from members')
	members = [dict(imageref=row[0], name=row[1], about=row[2], joined=row[3]) for row in cur.fetchall()]
	g.db.close()
	return render_template('members.html', members = members)

@app.route('/info')
def info():
	return render_template('info.html')

@app.route('/activities')
def activities():
	g.db = connect_db()
	cur = g.db.execute('select * from parties')
	parties = [dict(name=row[0], year=row[1], link=row[2]) for row in cur.fetchall()]
	g.db.close()
	return render_template('/activities.html', parties=parties)

if __name__ == '__main__':
	app.run(debug=True)
