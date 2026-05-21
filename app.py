from flask import Flask,render_template,request,redirect,url_for
import pymysql
app = Flask(__name__)


def connect_db():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="tharoth"
    )

    return connection  


@app.route("/")
def read ():
    myconnection = connect_db()
    cursor = myconnection.cursor()

    cursor.execute("SELECT * FROM students ")
    mystudent = cursor.fetchall()

    return render_template("index.html",mystudent=mystudent)


@app.route('/insert' , methods=["POST"])
def insert():
    conection = connect_db()
    cursor = conection.cursor()

    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']

    sql  = "INSERT INTO students (name,age,gender) values (%s,%s,%s) "
    cursor.execute(sql,(name,age,gender))
    conection.commit()

    return redirect(url_for('read'))


if __name__=="__main__":
    app.run(debug=True)

