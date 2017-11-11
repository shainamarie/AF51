from flask import Flask, render_template


app = Flask(__name__)


@app.route('/landing')
def landing():
    return render_template('mainlanding.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/logs')
def logs():
    return render_template('logs.html')


@app.route('/query')
def query():
    return render_template('query.html')


@app.route('/user')
def user():
    return render_template('user.html')


if __name__ == "__main__":
    app.run(debug=True)



