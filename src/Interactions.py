import sqlite3

from datetime import datetime
from random import randrange

# script for login 
def login(email, pwd):

    # connect to database
    db = sqlite3.connect('../data/dry_dock.db')
    c  = db.cursor()

    # attempt to fetch corresponding User
    c.execute('SELECT Users from dry_dock WHERE email=? AND password=?', email, pwd)
    if c.fetchone() is not None:
        return "Welcome"
    else:
        return "Login failed"

    c.close()

def queueBoat(boatID, ownerID, timeRequested):
    # connect to database
    db = sqlite3.connect('../data/dry_dock.db')
    c  = db.cursor()
    rID  = randrange(10000000)
        
    # update database
    c.execute('INSERT INTO Requests VALUES (?,?,?,?)', (rID, boatID, timeRequested, 0))
    c.execute('UPDATE Users SET request_id=? WHERE user_id=?', rID, ownerID)
    c.close()

    return "Your request has been added to the queue! Request ID: " + str(rID)

# boatID not needed for only one boat per user
def dequeueBoat(boatID, ownerID, requestID):
    # connect to database
    db = sqlite3.connect('../data/dry_dock.db')
    c  = db.cursor()

    # update database
    c.execute('DELETE FROM Requests WHERE request_id=?', requestID)
    c.execute('UPDATA Users SET request_id=NULL WHERE user_id=?', ownerID)
    c.close()

    return "Your request has been completed, thank you for choosing our marina!"
