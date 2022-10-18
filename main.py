import sqlite3 as sql
import logging
from rich.logging import RichHandler
import argparse
from pick import pick
from keyboard import getkey
from rich.console import Console
from rich.table import Table

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
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
    log.info(f"Connected to db {args['new']}")
    cur.execute("CREATE TABLE IF NOT EXISTS inventory(Category, Item, Quantity, Location)")
    con.commit()
else:
    con = sql.connect(f"{args['open']}")
    log.info(f"Connected to db {args['open']}")
    cur = con.cursor()

def categorySelect():
    title = "Select a category or multiple from the list below..."
    db_out = cur.execute("SELECT DISTINCT category from inventory").fetchall()
    options = [category[0] for category in db_out]
    options = sorted(options)
    selection = pick(options, title, multiselect=True, min_selection_count=1)
    logging.info(f"Selected categories: {selection}")
    return selection

# State loop
while True:
    # Determine next state
    print("Do you want to (s)earch, (u)pdate, or (q)uit")
    while True:
        match getkey():
            case 's':
                #print out categories and have user select
                title = "Select please lord select a god damn thingy..."
                targeted_categories = categorySelect()
                db_out = []
                for category in targeted_categories:
                    db_out.append(cur.execute("SELECT * from inventory WHERE category = ?", (category[0],)).fetchall())
                for category in db_out:
                    table = Table(title=f"{category[0][0]}")
                    table.add_column("ITEM")
                    table.add_column("QUANTITY")
                    table.add_column("LOCATION")
                    for item in category:
                        table.add_row(item[1], item[2], item[3])
                    console = Console()
                    console.print(table)
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

