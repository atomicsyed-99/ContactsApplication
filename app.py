from flask import Flask,flash, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
app = Flask(__name__)
  

app.secret_key = 'syed'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'geeklogin'

mysql = MySQL(app)





  
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts1 WHERE email = % s AND password = % s', (email, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect email / password !'
    return render_template('login.html', msg = msg)
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/Index')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts = data)

@app.route('/index',methods=['GET','POST'])
def index():
    msg=''
    if request.method=='POST' and 'name' in request.form and 'PhNo' in request.form and 'Email' in request.form:
        name=request.form['name']
        PhNo=request.form['PhNo']
        Email=request.form['Email']
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM contacts WHERE Email = % s',(Email,))
        account=cursor.fetchone()
        if account:
            flash('Contact already exists!')
            return redirect(url_for('Index'))
        else:
            cursor.execute('INSERT INTO contacts VALUES (NULL,%s,%s,%s)',(name,PhNo,Email,))
            mysql.connection.commit()
            flash('Contact successfully added!')
            return redirect(url_for('Index'))
            
    elif request.method=='POST':
        flash('Please add the contact details in the form!')
        return redirect(url_for('Index'))
    return render_template('index.html',msg=msg)
    




@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form and 'secret' in request.form :
        email = request.form['email']
        password = request.form['password']
        secret = request.form['secret']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts1 WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        #elif not re.match(r'[A-Za-z0-9]+', secret): the secret was originally username here
        #    msg = 'Secret key must contain only characters and numbers !'
        elif not secret or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts1 VALUES (NULL, % s, % s, % s)', (email, password, secret, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)



@app.route('/reset_password',methods=['GET','POST'])
def reset_request():
    msg=''
    if request.method == 'POST' and 'email' in request.form :
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts1 WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            
            msg="Reset Request sent!.Please check your mail!"
            
            

            #return render_template('reset_request.html',title='Reset Request',legend="Reset Password",msg=msg)
                
        else:
            msg = 'This user is not registered with us! . Please register!'
    return render_template('reset_request.html',title='Reset Request',legend="Reset Password",msg=msg)

@app.route('/display',methods=['GET','POST'])
def display():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM contacts')
    data=cursor.fetchall()
    return render_template('table.html',contacts=data)
