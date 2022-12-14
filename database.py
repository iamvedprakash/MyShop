# users (id integer primary key autoincrement, user varchar not null unique, phone int not null unique, address varchar not null, password varchar not null)
# items ( id integer primary key autoincrement, item varchar not null unique, category varchar not null, amount int not null, url varchar not null unique)
# orders (id integer primary key autoincrement, category varchar not null, item varchar not null, quantity int not null, amount int not null, order_by varchar not null, order_date varchar not null, status varchar not null;)




import sqlite3

connection = sqlite3.connect("database.db")
cur = connection.cursor()

#data = cur.execute("insert into items (item, category, amount, url) values ('Grape', 'fruit', 40, 'grape.jpg');")
#connection.commit()

data = cur.execute("select * from items")
print(data.fetchall())

connection.close()
