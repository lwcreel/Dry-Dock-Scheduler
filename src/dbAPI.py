import sqlite3
import os.path

from datetime import datetime
from random import randrange

path = os.path.abspath('../data/dry_dock.db')

# DO NOT LET THIS GO TO PRODUCTION W/O STORING PWDS AS SALTED HASHES

# script for login 
def login(name, pwd):

    # connect to database
    db = sqlite3.connect(path)
    c  = db.cursor()

    # attempt to fetch corresponding User
    c.execute('SELECT name, password FROM Users WHERE name=? AND password=?', (name, pwd))
    if c.fetchone() is not None:
        return True
    else:
        return False

    db.commit() 
    db.close()

def queueBoat(boatID, ownerID, timeRequested):
    # connect to database
    db = sqlite3.connect(path)
    c  = db.cursor()
    rID  = randrange(10000000)
        
    # update database
    c.execute('INSERT INTO Requests VALUES (?,?,?,?)', (rID, boatID, timeRequested, 0))
    c.execute('UPDATE Users SET request_id=? WHERE user_id=?', (rID, ownerID))
    db.commit() 
    db.close()

    return "Your request has been added to the queue! Request ID: " + str(rID)

# boatID not needed for only one boat per user
def dequeueBoat(boatID, ownerID, requestID, location):
    # connect to database
    db = sqlite3.connect(path)
    c  = db.cursor()

    # update database
    c.execute('DELETE FROM Requests WHERE request_id=?', requestID)
    c.execute('UPDATE Users SET request_id=NULL WHERE user_id=?', ownerID)
    db.commit() 
    db.close()

    clearSlip(location)

    return "Your request has been completed, thank you for choosing our marina!"

# create user
def createUser(name, email, pwd):
    # connect to database
    db = sqlite3.connect(path)
    db.set_trace_callback(print)
    c  = db.cursor()
    uID = randrange(10000000)

    c.execute('INSERT INTO Users (name, email, password, user_id) VALUES (?,?,?,?)', (name, email, pwd, uID)) # change to hash
    db.commit() 
    db.close()

    return "Success! User created successfully"

# create boat
def createBoat(makeAndModel, ownerName, yearMade, dockLocation, ownerID):
    # connect to database
    db = sqlite3.connect(path)
    c  = db.cursor()
    bID = randrange(10000000)

    # update database
    c.execute('INSERT INTO Boats VALUES (?,?,?,?,?)', (makeAndModel, ownerName, bID, yearMade, dockLocation))
    c.execute('UPDATE Users SET boat_id=? WHERE user_id=?', (bID, ownerID))
    db.commit() 
    db.close()

    return "Success! Boat linked to your account"

# move boat to new slip
def moveBoat(boatID, newLocation):
    db = sqlite3.connect(path)
    c  = db.cursor()
    c.execute('UPDATE Boats SET location=? WHERE id=?', (newLocation, boatID))
    db.commit() 
    db.close()

    return "boat moved"

# clear slip
def clearSlip(location):
    db = sqlite3.connect(path)
    c  = db.cursor()
    c.execute('UPDATE Slips SET boat_id=NULL WHERE location=?', location)
    db.commit() 
    db.close()

    return "slip cleared"

