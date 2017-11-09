from flask import Flask,render_template,session,request,redirect,url_for,g
import psycopg2
import os
app=Flask(__name__)
app.secret_key = os.urandom(24)







@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        session.pop('user', None)
        user_candidate= request.form['username']
        pass_candidate = request.form['password']
        conn = psycopg2.connect("dbname = 'pass_db' user = 'postgres' password = 'everboy' host = 'localhost' port = '5432'")
        cur = conn.cursor()
        user1=cur.execute('SELECT * from users where user_id = %s', (user_candidate,))
        pass1=cur.execute('SELECT * FROM users WHERE pass = %s',(pass_candidate,))
        data=cur.fetchone()
        conn.close()
        print(data)
        try:
            if user_candidate is '':
                return render_template("req_username.html")
            elif pass_candidate is '':
                return render_template("req_password.html")
            elif user_candidate not in data and pass_candidate not in data:
                session['user'] = request.form['username']
                return render_template("error_input.html")
            elif user_candidate  in data and pass_candidate  in data:
                session['user'] = request.form['username']
                return render_template("landing.html")
            elif user_candidate not in username:
                return render_template("error_input.html")
        except Exception:
            return render_template("error_input.html")
    else:
        return render_template("login.html")

@app.route('/landing')
def landing():
    if g.user:
        return render_template("landing.html")

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

@app.route('/test')
def test1():
    return render_template("req_password.html")


if __name__=="__main__":
    app.run(debug=True)
