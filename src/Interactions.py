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

def queueBoat(boatID, ownerID, timeRequested):
    # connect to database
    db = sqlite3.connect('../data/dry_dock.db')
    c  = db.cursor()
    rID  = randrange(10000000)

    c.execute('Select Users from dry_dock WHERE user_id=?', ownerID)

    if c.fetchone is not None:
        
        # create row in request table
        c.execute('INSERT INTO Requests VALUES (?,?,?,?)', (rID, boatID, timeRequested, 0))

        # update user with request number
        c.execute('UPDATE Users SET request_id=? WHERE user_id=?', rID, ownerID)

        return "Your request has been added to the queue! Request ID: " + str(rID)
    else:
        return "ERROR: user not known"

    


def dequeueBoat(boatID, requestID):
    pass


