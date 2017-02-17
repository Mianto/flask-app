from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey!!'

# login requires decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kargs):
        if 'LOGGED_IN' in session:
            return f(*args, **kargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credential.Please try again.'
        else:
            session['LOGGED_IN'] = True
            flash('You are now logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error = error)

@app.route('/logout')
@login_required
def logout():
    session.pop('LOGGED_IN', None)
    flash('You were just logged out')
    return redirect(url_for('welcome'))

if __name__ =='__main__' :
    app.run(debug = True)


