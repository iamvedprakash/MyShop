# All DB operations are performed here

import sqlite3

def checklogin(user, password):
    try:
        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        cur.execute("select count(*) from users where user=(?) and password=(?);",(user, password))
        count = cur.fetchone()
        if(count[0]==1):
            return True
        else:
            return False   
    except:
        return False
    finally:
        connection.close()

def adduser(user, phone, address, password):
    try:
        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        count = cur.execute("insert into users (user, phone, address, password) values (?,?,?,?);",(user, int(phone), address, password))

        if(count.rowcount == 1):
            connection.commit()
            return True
        else:
            return False
    except:
        connection.rollback()
        return False
    finally:
        connection.close()

def fetchitems():
    try:
        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        cur.execute("select * from items;")
        data = cur.fetchall()
        return data
    except:
        return None
    finally:
        connection.close()

def fetchorderhistory(user):
    try:
        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        cur.execute("select * from orders where order_by=(?);", (user,))
        data = cur.fetchall()
        data = data[::-1]
        return data
    except:
        return None
    finally:
        connection.close()

def addorder(category, item, quantity, amount, order_by, order_date, status):
    try:
        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        count = cur.execute("insert into orders (category, item, quantity, amount, order_by, order_date, status) values (?,?,?,?,?,?,?);",(category, item, int(quantity), int(amount), order_by, order_date, status))
        if(count.rowcount==1):
            connection.commit()
            return True
        else:
            return False
        
    except:
        return False
    finally:
        connection.close()

def getcategory():
    try:
        connection = sqlite3.connect("database.db")
        cur = connection.cursor()
        cur.execute("select distinct category from items;")
        data = cur.fetchall()
        return data
    except:
        return None
    finally:
        connection.close()