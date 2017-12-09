from flask import Flask,render_template
import psycopg2

app=Flask(__name__)

def create_table():
    conn=psycopg2.connect("dbname='forms' user='postgres' password='everboy' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS form(name Varchar, amount integer )")
    conn.commit()
    conn.close()



@app.route("/")
def search():
    conn=psycopg2.connect("dbname='forms' user='postgres' password='everboy' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT name from form")
    rows=cur.fetchall()
    rows=[i[0] for i in rows]
    return render_template("form.html",rows=rows)

if __name__=="__main__":
    app.run(debug=True)
