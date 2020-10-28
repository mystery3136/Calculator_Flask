from flask import Flask,render_template,redirect,request

app=Flask(__name__)

friends=["Aramun Haesulla","Tagon Niruha","Inaisingi","Jung Tae ul"]
num=5

@app.route('/')
def hello():
	return render_template("index.html",my_friends=friends,number=num)

@app.route('/home')
def home():
	return redirect('/')

@app.route('/about')
def about():
	return "About Page"

@app.route('/submit', methods=['POST'])
def submit_data():
	if request.method=='POST':
		number_1=int(request.form['number 1'])
		number_2=int(request.form['number 2'])
		operation=str(request.form['operation'])

		# f=request.files['userfile']
		# f.save(f.filename)

		if operation=="add":
			return str(number_1+number_2)
		elif operation=="subtract":
			return str(number_1-number_2)
		elif operation=="multiply":
			return str(number_1*number_2)
		elif operation=="divide":
			return str(number_1/number_2)

	

if __name__ == '__main__':
	app.run(debug=True)