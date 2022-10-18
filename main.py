import sqlite3 as sql
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--new", required=False, help="creates a new db with given name")
ap.add_argument("-o", "--open", required=False, help="opens existing db for viewing or editing")
args = vars(ap.parse_args())

if args['new']:
    con = sql.connect(f"{args['new']}")
    cur = con.cursor()
    cur.execute("CREATE TABLE categories(category, itemid)")
    con.commit()
else:
    con = sql.connect(f"{args['open']}")
    cur = con.cursor()
