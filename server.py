from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

data = [
	{
		"Title": "GA",
		"image": "/static/ga.jpg",
		"audio": "static/ga.mp3"
	},
	{
		"Title": "GB",
		"image": " /static/gb.jpg",
		"audio": "static/gb.mp3"

	},
	{
		"Title": "GC",
		"image": " /static/gc.jpg",
		"audio": "static/gc.mp3"

	},
	{
		"Title": "GD",
		"image": " /static/gd.jpg",
		"audio": "static/gd.mp3"

	},
	{
		"Title": "DE",
		"image": " /static/de.jpg",
		"audio": "static/de.mp3"
	},
	{
		"Title": "DF",
		"image": " /static/df1.jpg",
		"audio": "static/df1.mp3"
	},
	{
		"Title": "DG",
		"image": " /static/dg.jpg",
		"audio": "static/dg.mp3"
	},
	{
		"Title": "DA",
		"image": " /static/da.jpg",
		"audio": "static/da.mp3"

	},
	{
		"Title": "AB",
		"image": " /static/ab.jpg",
		"audio": "static/ab.mp3"

	},
	{
		"Title": "AC",
		"image": " /static/ac.jpg",
		"audio": "static/ac1.mp3"

	},
	{
		"Title": "AD",
		"image": " /static/ad.jpg",
		"audio": "static/ad.mp3"
	},
	{
		"Title": "AE",
		"image": " /static/ae.jpg",
		"audio": "static/ae.mp3"
	},
	{
		"Title": "EF",
		"image": " /static/ef1.jpg",
		"audio": "static/ef.mp3"
	},
	{
		"Title": "EG",
		"image": " /static/eg1.jpg",
		"audio": "static/eg.mp3"
	
	},
	{
		"Title": "EA",
		"image": " /static/ea.jpg",
		"audio": "static/ea.mp3"
	},
	{
		"Title": "EB",
		"image": " /static/eb.jpg",
		"audio": "static/eb.mp3"
	}


]




@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/home')
def home(name=None):
	return render_template('home.html') 


@app.route('/learn')
def learn(name=None):
	return render_template('learn.html', data=data) 


@app.route('/quiz', methods = ['GET', 'POST'])
def quiz(name=None):
	return render_template('quiz.html') 

@app.route('/quiz1', methods = ['GET', 'POST'])
def quiz1(name=None):
	return render_template('quiz1.html') 

@app.route('/quiz2', methods = ['GET', 'POST'])
def quiz2(name=None):
	return render_template('quiz2.html') 

@app.route('/quiz3', methods = ['GET', 'POST'])
def quiz3(name=None):
	return render_template('quiz3.html') 

@app.route('/result', methods = ['GET', 'POST'])
def result(name=None):
	return render_template('result.html') 



if __name__ == '__main__':
   app.run(debug = True)
