from flask_app import app
from flask import render_template, request, redirect, session
from random import randint

#public routes
@app.route('/')
def index():
    if 'random_num' not in session:
        session['random_num'] = randint(1,100)
    print(session['random_num'])
    return render_template('index.html')




#hidden routes
@app.route('/submit_num', methods=['POST'])
def submit_num():
    session['guessed_num'] = int(request.form['guessed_num'])
    print(session['guessed_num'])
    return redirect('/')