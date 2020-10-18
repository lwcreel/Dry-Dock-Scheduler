import sqlite3

# script for login 
def login(email, pwd):

    # connect to database
    db = sqlite3.connect('../data/dry_dock.db')
    c  = db.cursor()

    # attempt to fetch corresponding User
    c.execute('SELECT Users from dry_dock WHERE email = "%s" AND password="%s"' %(email, pwd))
    if c.fetchone() is not None:
        return "Welcome"
    else:
        return "Login failed"

