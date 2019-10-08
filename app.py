from flask import Flask, render_template, session, request
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Leyno'

vorur=[
	[0,"Pop-eye",6000,"pop-eye.jpg"],
	[1,"Captain hook",3000,"hook.jpg"],
	[2,"Totally Normal baby",500,"normal.jpg"],
	[3,"Winnie the Pooh",5500,"pooh.jpg"],
	[4,"Prisoner",3200,"prison.jpg"],
	[5,"Taco de bebe",4350,"taco.jpg"]
]


@app.route('/')
def index():
	karfa = 0
	if 'karfa' in session:
		karfa = len(session['karfa'])
		til = True
	else:
		til = False
	return render_template("index.html", vorur=vorur, k=karfa, til=til)


@app.route('/ikorfu/<int:id>')
def ikorfu(id):
	karfa = []
	if 'karfa' in session:
		karfa = session['karfa']
		karfa.append(id)
		session['karfa'] = karfa
	else:
		karfa.append(id)
		session['karfa'] = karfa
	print(len(karfa))
	return render_template("ikorfu.html", vorur=vorur)


@app.route('/karfa')
def karfa():
	karfa = []
	k=0
	heild=0
	if 'karfa' in session:
		karfa = session['karfa']
		k = len(session['karfa'])
		for x in karfa:
			for y in vorur:
				if y[0] == x:
					heild += y[2]
	return render_template("karfa.html", vorur=vorur, karfa=karfa, k=k, heild=heild)


@app.route('/eyda/<int:id>')
def eyda(id):
	karfa = []
	if 'karfa' in session:
		karfa = session['karfa']
		karfa.remove(id)
		session['karfa'] = karfa
	return render_template("eyda.html", vorur=vorur)

@app.route('/taema')
def taema():
	session.pop('karfa',None)
	return render_template("taema.html", vorur=vorur)

@app.route('/karfa/kaupa')
def kaupa():
	karfa = []
	heild = 0
	if 'karfa' in session:
		karfa = session['karfa']
		for x in karfa:
			for y in vorur:
				if y[0] == x:
					heild += y[2]
	return render_template("kaupa.html", vorur=vorur, karfa=karfa, heild=heild)

@app.route('/karfa/kaupa/takk', methods=['GET','POST'])
def takk():
	if request.method == 'POST':
		nafn = request.form['name']
		netfang = request.form['email']
	karfa = []
	session['karfa'] = karfa
	return render_template("takk.html", vorur=vorur, nafn=nafn, netfang=netfang)

@app.errorhandler(404)
def error404(error):
	return "Síða ekki fundin", 404

if __name__ == "__main__":
	app.run(debug=True)