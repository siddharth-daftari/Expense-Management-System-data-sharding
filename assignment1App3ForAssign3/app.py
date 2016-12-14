from flask import Flask,json,request,jsonify,session,Response
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from sqlalchemy.sql.expression import func

app = Flask(__name__)

import sqlalchemy
USER = "root"
PASSWORD = "pass1234"
HOSTNAME = "db3"
DATABASE = "EMS"
engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME))
engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE))

#dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Emstable1(db.Model):
	id = db.Column("id",db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(50))  
	category = db.Column(db.String(100))
	description = db.Column(db.String(1000))
	link = db.Column(db.String(100))
	estimated_costs = db.Column(db.String(10))
	submit_date = db.Column(db.String(10))
	status = db.Column(db.String(100))
	decision_date = db.Column(db.String(10))

	def __init__(self, id, name, email, category,description,link,estimated_costs,submit_date,status,decision_date):
		self.id = id
		self.name = name
		self.email = email
		self.category = category
		self.description = description
		self.link = link
		self.estimated_costs = estimated_costs
		self.submit_date = submit_date
		self.status = status
		self.decision_date = decision_date

@app.route('/v1/expenses/<expense_id>',methods=['GET'])
def retrieveData(expense_id):
	
	#select record for given expense_id
	result = Emstable1.query.filter_by(id=expense_id).first_or_404()
	
	#build response json variable
	responsetempVar = {
		"id" : result.id,
		"name" : result.name,
		"email" : result.email,
		"category" : result.category,
		"description" : result.description,
		"link" : result.link,
		"estimated_costs" : result.estimated_costs,
		"submit_date" : result.submit_date,
		"status" : result.status,
		"decision_date" : result.decision_date
	}
	
	#add/modify properties of response variable 
	response = jsonify(responsetempVar)
	
	#return the response object
	return response

@app.route("/v1/expenses",methods=['POST'])
def insertData():
	
	#insert new record 
	request_data = request.get_json(force=True)
	
	tempVar = Emstable1(request_data['id'], request_data['name'],request_data['email'],request_data['category'],request_data['description'],request_data['link'],request_data['estimated_costs'],request_data['submit_date'],"pending|approved|rejected|overbudget",date.today())
	db.session.add(tempVar)
	db.session.commit()
	
	#select max id from table i.e. id for record that was just inserted above
	max_id = db.session.query(func.max(Emstable1.id).label("max_1")).first().max_1
	result = Emstable1.query.filter_by(id=max_id).first_or_404()
	
	#build response json variable
	responsetempVar = {
		"id" : result.id,
		"name" : result.name,
		"email" : result.email,
		"category" : result.category,
		"description" : result.description,
		"link" : result.link,
		"estimated_costs" : result.estimated_costs,
		"submit_date" : result.submit_date,
		"status" : result.status,
		"decision_date" : result.decision_date
	}
	
	#add/modify properties of response variable 
	response = jsonify(responsetempVar)
	response.headers['location'] = '/v1/expenses/' + str(result.id)	
	response.status_code = 201
	
	#return the response object
	return response

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True,host="0.0.0.0",port=5003)
