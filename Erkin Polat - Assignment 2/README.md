# CS162 - Web application - Kanban Board
## Features of the App:
This is a Kanban Board that you can use to keep track of your tasks. You can add new tasks and move them around the sections. You can also remove tasks from the board. 

## General Structure
The app consists of a python file that runs flask. An html file for the main page and a database file.

Inside the python file I specified the different functionalities that should be performed with the app. These are add, move_right, move_back and delete. I use SQLAlchemy on a SQLite database. For all of my database entries I have a text for the name of the task and a completion number. 0 means incomplete, 1 means in progress and 2 means completed. These are rendered in the html file into 3 columns for each of these categories.

I used this youtube tutorial as a resource, but then built on the main concepts introduced here : https://www.youtube.com/watch?v=4kD-GRF5VPs&t=497s


## How to run:
Install the files. Set your directory properly and then go to your terminal and type the following lines. Based on the version of python you are using the first command could be different.

python3.6 -m venv .venv 
source .venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=app.py
flask run

## Testing:
For testing I tried to adapt code from multiple resources I found. However the final code seems to have some problems. In general I created methods under the TestApp class for every route I normally have in my application. For each of them I send a sample request with the given function to the proper route and then check if the status code returns as 200 which means the request had succeeded. 

Sources:
https://flask.palletsprojects.com/en/1.1.x/testing/
https://damyanon.net/post/flask-series-testing/
https://medium.com/@neeti.jain/how-to-do-unit-testing-in-flask-and-find-code-coverage-fa5201399bc4
https://www.patricksoftwareblog.com/unit-testing-a-flask-application/

