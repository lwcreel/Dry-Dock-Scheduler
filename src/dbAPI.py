import sqlite3
import os.path

from datetime import datetime
from random import randrange

path = os.path.abspath('dry_dock.db')

# DO NOT LET THIS GO TO PRODUCTION W/O STORING PWDS AS SALTED HASHES

# script for login 
def login(name, pwd, is_worker):

    # connect to database
    db = sqlite3.connect(path)
    c  = db.cursor()

    # attempt to fetch corresponding User
    c.execute('SELECT name, password, is_worker FROM Users WHERE name=? AND password=? AND is_worker=?', (name, pwd, is_worker))
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
def dequeueBoat(boatID):
    # connect to database
    db = sqlite3.connect(path)
    c  = db.cursor()

    # update database
    c.execute('DELETE FROM Requests WHERE boat_id=?', (boatID,))
    c.execute('UPDATE Users SET request_id=NULL WHERE boat_id=?', (boatID,))
    c.execute('UPDATE Boats SET location=1 WHERE id=?', (boatID,))
    db.commit() 
    db.close()

    return "Your request has been completed, thank you for choosing our marina!"

# create user
def createUser(name, email, pwd, cpwd, isWorker):
    # connect to database
    db = sqlite3.connect(path)
    db.set_trace_callback(print)
    c  = db.cursor()
    uID = randrange(10000000)
    c.execute('SELECT name, email FROM Users WHERE name=? OR email=?', (name, email))
    if c.fetchone() is not None:
        return False
    else:
        if (pwd == cpwd) and (name != '') and (email != '') and (pwd != '') and (cpwd != ''):
            if (isWorker):
                c.execute('INSERT INTO Users (name, email, password, user_id, is_worker) VALUES (?,?,?,?,1)', (name, email, pwd, uID)) # change to hash
                db.commit() 
                db.close()
                return True
            else:
                c.execute('INSERT INTO Users (name, email, password, user_id, is_worker) VALUES (?,?,?,?,0)', (name, email, pwd, uID)) # change to hash
                db.commit() 
                db.close()
                return True
        else:
            return False
#might be unnecessary, tried to merge with createUser
def createWorker(name, email, pwd):
    # connect to database
    db = sqlite3.connect(path)
    db.set_trace_callback(print)
    c  = db.cursor()
    uID = randrange(10000000)

    c.execute('INSERT INTO Users (name, email, password, user_id, is_worker) VALUES (?,?,?,?,1)', (name, email, pwd, uID)) # change to hash
    db.commit() 
    db.close()

    return "Success! User created successfully"


# create boat
def createBoat(makeAndModel, ownerName, yearMade, dockLocation):
    # connect to database
    db = sqlite3.connect(path)
    c  = db.cursor()
    bID = randrange(10000000)

    # update database
    c.execute('INSERT INTO Boats VALUES (?,?,?,?,?)', (makeAndModel, ownerName, bID, yearMade, dockLocation))
    c.execute('UPDATE Users SET boat_id=? WHERE name=?', (bID, ownerName))
    db.commit() 
    db.close()

    return bID

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


def getStatus(username):
    db = sqlite3.connect(path)
    c = db.cursor()
    c.execute('SELECT location FROM Boats WHERE owner_name=?', (username,))
    value = c.fetchone()
    db.close()
    return value[0]

def changePassword(username, email, password, cpassword):
    db = sqlite3.connect(path)
    c = db.cursor()

    # attempt to fetch corresponding User
    c.execute('SELECT name, email FROM Users WHERE name=? AND email=?', (username, email))
    if c.fetchone() is not None:
        # update if valid
        if(password == cpassword):
            c.execute('UPDATE Users SET password=? WHERE name=? AND email=?', (password, username, email))
            db.commit()
            db.close()
            return True
        else:
            return False
    else:
        return False

def getBoatID(username):
    db = sqlite3.connect(path)
    c = db.cursor()
    c.execute('SELECT boat_id FROM Users WHERE name=?', (username,))
    value = c.fetchone()
    if value is not None:
        db.close()
        return value[0]