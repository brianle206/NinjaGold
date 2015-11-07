from flask import Flask, redirect, render_template, session, request
import random
from datetime import datetime
time = datetime.now()
app = Flask(__name__)
app.secret_key = "Top_Secret"


@app.route('/')
def index():
	try:
		session['gold']
		session['msg']
	except:
		session['gold'] = 0
		session['msg'] = []
 	return render_template("index.html", gold=session['gold'], msg=session['msg'])

@app.route('/process_money', methods=['POST'])
def datmonie():
	if request.form['building'] == 'farm':
		session['makemoney1'] = random.randrange(10,21)
		session['gold'] += session['makemoney1']
		note = "Earned %d golds from farming shit %s" %(session['makemoney1'], time)
		session['msg'].append(note)
	elif request.form['building'] == 'cave':
		session['makemoney2'] = random.randrange(5,11)
		session['gold'] += session['makemoney2']
		note = "Earned %d golds from caving shit %s" %(session['makemoney2'], time)
		session['msg'].append(note)
	elif request.form['building'] == 'house':
		session['makemoney3'] = random.randrange(2,6)
		session['gold'] += session['makemoney3']
		note = "Earned %d golds from housing shit %s" %(session['makemoney3'], time)
		session['msg'].append(note)
	else:
		session['makemoney4'] = random.randrange(-50,50)
		session['gold'] += session['makemoney4']
		if session['makemoney4'] > 0 :
			note = "Yo youz lucky %d golds from casinoing shit %s" %(session['makemoney4'], time)
			session['msg'].append(note)

		else:
			note = "You Suck Yo wife gonna kill you, lost %d golds mang %s" %(session['makemoney4'], time)
			session['msg'].append(note)

	return redirect('/')

app.run(debug=True)