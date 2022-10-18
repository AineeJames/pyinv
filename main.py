import sqlite3 as sql
import logging
import argparse
from pick import pick
from keyboard import getkey
logging.basicConfig(format='%(asctime)s - %(name)s:%(levelname)s:%(message)s', level=logging.INFO)


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

# State loop
while True:
    # Determine next state
    print("Do you want to (s)earch, (u)pdate, or (q)uit")
    while True:
        key = getkey()
        match key:
            case 's':
                print("pressed s")
                #print out categories and have user select
                title = "Select please lord select a god damn thingy..."
                options = ["lol", "uwont", "xd"]
                selection = pick(options, title, multiselect=True, min_selection_count=1)
                print(selection)
                #print out items w/ quantity and location
                break
            case 'u':
                print("pressed u")
                while True:
                    match getkey():
                        case 'e':
                            pass
                        case 'r':
                            pass
                        case 'n':
                            pass
                        case _:
                            pass
            case 'q':
                print("Closing...")
                exit()
            case _:
                pass

