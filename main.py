import sqlite3 as sql
import logging
import argparse

logging.basicConfig(format='%(asctime)s - %(name)s:%(levelname)s:%(message)s', level=logging.DEBUG)
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--new", required=False, help="creates a new db with given name")
ap.add_argument("-o", "--open", required=False, help="opens existing db for viewing or editing")
args = vars(ap.parse_args())

if not args['new'] and not  args['open']:
    print("you dummy trash")
    exit()

if args['new']:
    con = sql.connect(f"{args['new']}")
    cur = con.cursor()
    logging.info(f"Connected to db {args['new']}")
    cur.execute("CREATE TABLE IF NOT EXISTS items(category, item, quantity, location)")
    con.commit()
else:
    con = sql.connect(f"{args['open']}")
    logging.info(f"Connected to db {args['open']}")
    cur = con.cursor()
