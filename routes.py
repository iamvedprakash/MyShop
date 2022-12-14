from flask import Flask, request, json, session, redirect, url_for, render_template
from datetime import date
import dboperations


app = Flask(__name__) 

items = dboperations.fetchitems()
if items != None:
    items = json.dumps(items)
else:
    items = "Something went wrong"

category = dboperations.getcategory()
category = json.dumps(category)


@app.route('/', methods=['POST', 'GET'])
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    else:
        if request.method=="POST":
            user = request.form['username']
            password = request.form['password']
            status = dboperations.checklogin(user, password)
            if status:
                session['user'] = user
                return redirect(url_for('home'))
            else:
                #call with error message
                return render_template('login.html', items=items, category = category, loginerror=1)
        else:
            #call login page
            return render_template('login.html', items=items, category = category, loginerror=0)

@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user', None)
    return redirect(url_for('login'))

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if 'user' in session:
        return redirect(url_for('home'))
    else:
        if request.method=="POST":
            user = request.form['username']
            phone = request.form['phone']
            address = request.form['address']
            password = request.form['password']
            confirm_password = request.form['confirm_password']
            if len(user)!=4 or not phone.isnumeric() or len(phone)!=5 or (password!=confirm_password) or len(password)<4:
                #reload signup with error message
                return render_template('signup.html', items=items, category = category, signuperror=1)
            else:
                status = dboperations.adduser(user, phone, address, password)
                if status:
                    session['user'] = user
                    return redirect(url_for('home'))
                else:
                    #reload sigup with user,phone not unique error
                    return render_template('signup.html', items=items, category = category, signuperror=2)
        else:
            #load signup page
            return render_template('signup.html', items=items, category = category, signuperror=0)

@app.route("/home", methods=["POST", "GET"])
def home():
    if 'user' in session:
        if request.method=='POST':
            datalist = request.get_json()
            today = str(date.today())

            for data in datalist.values():
                #dboperations.addorder(data['category'], data['item'], data['quantity'], data['amount'], session['user'], today, 'Placed')
                dboperations.addorder('None', data['classname'], data['quantity'], data['amount'], session['user'], today, 'Placed')
            
            #load home page
            return redirect(url_for('home'))
        else:
            #load home page
            return render_template('home.html', items=items, category = category,)
    else:
        return redirect(url_for('login'))

@app.route("/orders")
def orders():
    if 'user' in session:
        orders = dboperations.fetchorderhistory(session['user'])        
        if orders != None:
            orders = json.dumps(orders)
        else:
            orders = "Something went wrong"
        
        # load order page
        return render_template('order.html', orders=orders)
    else:
        return redirect(url_for('login'))

if __name__=="__main__":
    app.run(debug=True)