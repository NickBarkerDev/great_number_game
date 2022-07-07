from flask_app import app
from flask import render_template, request, redirect, session
from random import randint

#public routes
@app.route('/')
def index():
    session['random_num'] = randint(1,100)
    # print(session)
    return render_template('index.html')




#hidden routes
@app.route('/submit_num', methods=['POST'])
def submit_num():
    if
    pass
