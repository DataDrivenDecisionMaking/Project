from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('form.html')

@app.route('/signup', methods = ['POST'])
def signup():
    fullname = request.form['fullname']
    age = request.form['age']
    gender = request.form['gender']
    yearly_income = request.form['yearly_income']
    zipcode = request.form['zipcode']
    print("The name is '" + fullname + "'")
    print("The age is '" + age + "'")
    print("The yearly income is '" + yearly_income + "'")
    print("The zipcode is '" + zipcode + "'")
    print("The gender is '" + gender + "'")
    return redirect('/')
    
@app.route('/Next')
def healthinfo():
	return render_template('healthinfo.html')

if __name__ == "__main__":
    app.run()

