'''
Dev: cristian 
script description: sQlite3 base configuration
'''

# import ingine database package
import sqlite3

# create a database connection (DB Name)
con = sqlite3.connect('database-Exercise/market.db')

#cursor let us execute sql commands or operations (query)

cur = con.cursor()

#create  users table 
user_table = '''
CREATE TABLE IF NOT EXISTS users( 
    id INTEGER PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    ide_number VARCHAR(15) UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    status BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
    updated_at TIMESTAMP DEFAULT (datetime('now','localtime')),
    deleted_at TIMESTAMP NULL


);
'''
#Execute sql
cur.execute(user_table)

# save changes in database -> plush to database 
con.commit()