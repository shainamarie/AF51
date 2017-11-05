from flask import Flask,render_template,session,request,redirect,url_for,g,Blueprint
import psycopg2
import os
app=Flask(__name__)
auth_blueprint = Blueprint('auth_blueprint', __name__, template_folder='templates', static_folder='static',
                           static_url_path='/static/')

app.secret_key = os.urandom(24)






def select(password):
    conn = psycopg2.connect("dbname = 'pass_db' user = 'postgres' password = 'everboy' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute('SELECT pass from users where pass = %s', (password,))
    conn.close()
    return password


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        session.pop('user', None)
        pass1 = select(request.form['password'])
        if request.form['password'] == pass1:
            session['user'] = request.form['username']
            return redirect(url_for('about'))

    return render_template("login.html")

@app.route('/about')
def about():
    if g.user:
        return render_template("about.html")

    return redirect(url_for('home'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/logout')
def logout():
    session.pop('user',None)
    return 'dropped'


if __name__=="__main__":
    app.run(debug=True)
