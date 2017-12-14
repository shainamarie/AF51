from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request
from flask_bootstrap import Bootstrap
from forms import *
import string
from random import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:65413620@localhost:5432/mydb2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'flaskimplement'
app.debug = True
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)

    firstname = db.Column(db.String(80), unique=False)
    middlename = db.Column(db.String(80), unique=False)
    lastname = db.Column(db.String(80), unique=False)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=True)
    officerrole = db.Column(db.String(80), unique=False)

    def __init__(self, firstname='', middlename='', lastname='', username='', password='', officerole=''):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.username = username
        self.password = password
        self.officerrole = officerole

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/create')
def create():
    form = CreateAccount()
    return render_template('create.html', form=form)


@app.route('/createaccount', methods=['POST', 'GET'])
def createaccount():
    chars = string.ascii_letters + string.digits
    passwords = "".join(choice(chars) for x in range(randint(8, 10)))
    form = CreateAccount()
    if request.method == "POST":
        if form.validate_on_submit():
            if User.query.filter_by(username=form.username.data).first():
                msg = "Username Already Taken"
                return render_template('createresult.html', msg=msg)
            else:
                randompass = passwords
                user = User(firstname=form.firstname.data, middlename=form.middlename.data, lastname=form.lastname.data,
                            username=form.username.data, password=randompass, officerole=form.officerrole.data)
                db.session.add(user)
                db.session.commit()
                msg = "ADDED"
                note = randompass
                return render_template('result.html', msg=msg, note=note)

    return render_template('create.html', form=form)


@app.route('/print')
def printall():
    myUser = User.query.all()
    if myUser is None:
        msg = "NO ACCOUNTS FOUND"
        return render_template('result.html', msg=msg)
    else:
        return render_template('printfinal.html', myUser=myUser)


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == "POST":
        checker = request.form['usershit']
        if checker is not None:
            print 'HI'
            print checker
            msg = checker
            return render_template('result.html', msg=msg)
    msg = "NOTHING"
    return render_template('result.html', msg=msg)


if __name__ == "__main__":
    app.run()













