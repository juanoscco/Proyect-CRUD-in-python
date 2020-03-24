from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

from settings import SETTINGS


app = Flask(__name__)

# MySQL connection
app.config['MYSQL_HOST'] = SETTINGS["MYSQL_HOST"]
app.config['MYSQL_USER'] = SETTINGS["MYSQL_USER"]
app.config['MYSQL_PASSWORD'] = SETTINGS["MYSQL_PASSWORD"]
app.config['MYSQL_DB'] = SETTINGS["MYSQL_DB"]
mysql = MySQL(app)
# Settings
app.secret_key = SETTINGS["SECRET_KEY"]


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts=data)


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO contacts (fullname, phone, email) VALUES(%s, %s, %s)',
            (fullname, phone, email)
        )
        mysql.connection.commit()
        flash('Contact added Successfully')
    return redirect(url_for('index'))


@app.route('/edit/<contact_id>')
def get_contact(contact_id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (contact_id, ))
    data = cur.fetchall()
    return render_template('edit-contact.html', contact=data[0])


@app.route('/update/<contact_id>', methods=['POST'])
def update_contact(contact_id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE contacts
        SET fullname = %s,
            email = %s,
            phone = %s
        WHERE id = %s
    """, (fullname, email, phone, contact_id))
    mysql.connection.commit()
    flash('Contact Updated Successfully')
    return redirect(url_for('index'))


@app.route('/delete/<string:contact_id>')
def delete_contact(contact_id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id= %s', (contact_id, ))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=SETTINGS["PORT"], debug=SETTINGS["DEBUG"])
