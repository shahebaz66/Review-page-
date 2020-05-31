from flask import Flask, render_template, request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
app = Flask(__name__)
app.secret_key = 'this is my first flask app deployed using heroku owner shhahebaz'

env='pro'
if env=='dev':
	
	app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost/data'
	app.debug=True
else:
	app.debug=False
	app.config['SQLALCHEMY_DATABASE_URI']='postgres://qupfgvnqsstksr:eca0ab852ee5fbff171b9f6b8d76e5165b777f5738647df208265c8c4156b4a9@ec2-34-193-232-231.compute-1.amazonaws.com:5432/dfcs9oqidldmm8'
	

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class datas(db.Model):
	__tablename__='datat'
	id =db.Column(db.Integer,primary_key=True)
	first_name=db.Column(db.String)
	product=db.Column(db.String)
	review=db.Column(db.String)
	


	def  __init__(self,first_name,product,review):
		self.first_name=first_name
		self.product=product
		self.review=review


class datac(db.Model):
	__tablename__='customer'
	id =db.Column(db.Integer,primary_key=True)
	first_name=db.Column(db.String)
	Email=db.Column(db.String)
	Password=db.Column(db.String)
	


	def  __init__(self,first_name,Email	,Password):
		self.first_name=first_name
		self.Email=Email
		self.Password=Password












currentDT = datetime.datetime.now()
day=currentDT.day
month=currentDT.month
year=currentDT.year


@app.route('/')
def index():

		
	return render_template('index.html')
	

@app.route('/write', methods=['GET','POST'])
def write():
	msg=""
	data=datas.query.all()
	re=[]
	for dat in data:
		a=(dat.first_name,dat.product,dat.review)
		re.append(a)
	if request.method == 'POST' :
		
		
		
		first_name=request.form["Name"]
		product=request.form["Product"]
		review=request.form["Review"]

		data=datas(first_name,product,review)
		db.session.add(data)
		db.session.commit()
	
		data=datas.query.all()
		re=[]
		for dat in data:
			a=(dat.first_name,dat.product,dat.review)
			re.append(a)

		
		


			
		msg="Thank you for giving your valuable review pls scroll down to read your review"
		return  redirect(url_for('new'))
	
		
	
	return  render_template("index1.html" ,msg=msg,len=len(re),re = re,day=day,month=month,year=year)
		

@app.route('/new',methods=['GET'])
def new():
	data=datas.query.all()
	re=[]
	for dat in data:
		a=(dat.first_name,dat.product,dat.review)
		re.append(a)
	msg="Thank you for giving your valuable review pls scroll down to read your review"
	
	return  render_template("index1.html" ,msg=msg,len=len(re),re = re,day=day,month=month,year=year)

		



	
	

@app.route('/read')
def read():
	data=datas.query.all()
	re=[]
	for dat in data:
		a=(dat.first_name,dat.product,dat.review)
		re.append(a)

		
	return render_template("index2.html",len=len(re),re = re,day=day,month=month,year=year)




@app.route('/login',methods=['POST','GET'])
def login():
	if request.method=='POST':
		data=datac.query.all()
		re=[]
		for dat in data:
			a=(dat.first_name,dat.Email,dat.Password)
			re.append(a)
		
		for i,j,k in re:
			if i==request.form["Name"] and j==request.form["Email"] and k==request.form["Password"]:
				return redirect(url_for('write'))
		else:
			return render_template("index3.html",msg="incorrect details")
		
		
	return render_template("index3.html")
	




@app.route('/register',methods=['POST','GET'])
def register():
	if request.method=='POST':
		
		first_name=request.form["Name"]
		Email=request.form["Email"]
		Password=request.form["Password"]
				
		data=datac(first_name,Email,Password)
		db.session.add(data)
		db.session.commit()

				
		msg="Thank you for registering pls login"
		return render_template("index3.html",msg=msg)
	return render_template("index4.html")
	

if __name__ == '__main__':
        app.run()
