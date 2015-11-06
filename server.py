from flask import Flask, redirect, render_template, session, request
import random
app = Flask(__name__)
app.secret_key = "Top_Secret"


@app.route('/')
def index():
	try:
		session['gold']
	except:
		session['gold'] = 0
	
	return render_template("index.html", gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def datmonie():
	if request.form['building'] == 'farm':
		session['gold'] += random.randrange(10,20)
	elif request.form['building'] == 'cave':
		session['gold'] += random.randrange(5,10)
	elif request.form['building'] == 'house':
		session['gold'] += random.randrange(2,5)
	else:
		session['gold'] += random.randrange(0,50)
	return redirect('/')

app.run(debug=True)