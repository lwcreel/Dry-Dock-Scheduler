import sqlite3

# connect to database file
conn = sqlite3.connect('../data/dry_dock.db')
c = conn.cursor()

# commands to create tables, only run on re-deploy
c.execute("""CREATE TABLE DryDock (
    slip_id integer,
    request_id integer,
    )""")

# users can have one boat and request (as of right now)
c.execute("""CREATE TABLE Users (
    name text,
    email text,
    password text,
    user_id integer,
    boat_id integer,
    request_id integer
    )""")

# boats have one owner and one location
c.execute("""CREATE TABLE Boats (
    make_model text,
    owner_name text,
    id integer,
    year_made integer,
    location integer
    )""")

# a slip has only one boat and one location
c.execute("""CREATE TABLE Slips (
    boat_id integer,
    slip_id integer,
    location integer
    )""")

# push to .db file
conn.commit()

# housekeeping
conn.close()
