from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Erkin/Documents/School/CS Conc/CS162/Kanban/kanban.db'

#merge the database name with the name of the directory
db_path = os.path.join(os.path.dirname(__file__), 'kanban.db')

#turn into proper uri format
db_uri = 'sqlite:///{}'.format(db_path)

#set the uri
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

#Initialize the sqlalchemydatabase
db = SQLAlchemy(app)

#Create the table with proper columns. Every entry gets a unique id. They have names and completion statuses
class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(200))
	complete = db.Column(db.Integer)


#Creating the first route that is main page
@app.route('/')
def index():
	#Querying from the database for all 3 kinds of tasks based on their completion
	incomplete = Todo.query.filter_by(complete = 0).all()
	in_progress = Todo.query.filter_by(complete = 1).all()
	complete = Todo.query.filter_by(complete = 2).all()
	
	#Returns the rendered template with the appropriate tasks
	return render_template('index.html', incomplete=incomplete, in_progress = in_progress, complete=complete )


#Creating the add route to add new tasks.
@app.route('/add', methods=['POST', 'GET'])
def add():
	#Gets the item from the html form. Marks completion as incomplete
	todo = Todo(text=request.form['todoitem'], complete=0)
	
	#Adds item to the database
	db.session.add(todo)
	
	#Commits to the database
	db.session.commit()

	#Redirects to the homepage
	return redirect(url_for('index'))


#Route that moves things right takes a specific item with an id as input
@app.route('/move_right/<id>', methods = ['POST', 'GET'])
def move_right(id):
	
	#gets the first item from the query
	todo = Todo.query.filter_by(id = int(id)).first()
	
	#Adds one to the complete number
	todo.complete = todo.complete + 1
	
	#Commits into the session
	db.session.commit()

	#Redirects to the homepage
	return redirect(url_for('index'))


#Route and function to delete items. Again works with a specific id
@app.route('/delete/<id>', methods = ['POST', 'GET'])
def delete(id):

	#Gets item from the query
	todo = Todo.query.filter_by(id = int(id)).first()
	
	#Deletes the item
	db.session.delete(todo)
	
	#Commits into the session
	db.session.commit()

	#Redirects to the hompage
	return redirect(url_for('index'))


#Route and function to move items to the right
@app.route('/move_back/<id>', methods = ['POST', 'GET'])
def move_back(id):

	#Gets the first item from the query
	todo = Todo.query.filter_by(id = int(id)).first()
	
	#Decreases the todo count by 1
	todo.complete = todo.complete - 1
	
	#Commits into the session
	db.session.commit()

	#Redirects to the homepage
	return redirect(url_for('index'))
 
if __name__ == '__main__':
	app.run(debug=True)
