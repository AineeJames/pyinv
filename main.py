import sqlite3 as sql
import logging
import argparse

logging.basicConfig(format='%(asctime)s - %(name)s:%(levelname)s:%(message)s', level=logging.DEBUG)

import sys,tty,os,termios
def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    try:
        while True:
            b = os.read(sys.stdin.fileno(), 3).decode()
            if len(b) == 3:
                k = ord(b[2])
            else:
                k = ord(b)
            key_mapping = {
                127: 'backspace',
                10: 'return',
                32: 'space',
                9: 'tab',
                27: 'esc',
                65: 'up',
                66: 'down',
                67: 'right',
                68: 'left',
                113: 'q',
                117: 'u',
                115: 's'

            }
            return key_mapping.get(k, chr(k))
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


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
        match getkey():
            case 's':
                print("pressed s")
            case 'u':
                print("pressed u")
            case 'q':
                print("pressed q")
            case _:
                pass

