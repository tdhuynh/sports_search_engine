import psycopg2
import sys

# manually start:  pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

connection = psycopg2.connect("dbname=ufc_allweights_stats user=ufc_allweights_stats")
cursor = connection.cursor()


def first_name():
    first_name = input("First name: ").upper()
    cursor.execute("SELECT * from ufc_stats_table WHERE first_name = %s;", (first_name,))
    results = cursor.fetchall()
    for item in results:
        print("""
First name: {}
Last name: {}
Fights: {}
Strikes: {}
Strike accuracy: {}
Takedown: {}
Takedown accuracy: {}
Knockdowns: {}
Passes: {}
Reversals: {}
Submissions: {}
""".format(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11]))


def last_name():
    last_name = input("Last name: ").upper()
    cursor.execute("SELECT * from ufc_stats_table WHERE last_name = %s;", (last_name,))
    results = cursor.fetchall()
    for item in results:
        print("""
First name: {}
Last name: {}
Fights: {}
Strikes: {}
Strike accuracy: {}
Takedown: {}
Takedown accuracy: {}
Knockdowns: {}
Passes: {}
Reversals: {}
Submissions: {}
""".format(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11]))

def fights():
    fights = input("Fights: ")
    cursor.execute("SELECT * from ufc_stats_table WHERE fights = %s;", (fights,))
    results = cursor.fetchall()
    for item in results:
        print("""
First name: {}
Last name: {}
Fights: {}
Strikes: {}
Strike accuracy: {}
Takedown: {}
Takedown accuracy: {}
Knockdowns: {}
Passes: {}
Reversals: {}
Submissions: {}
""".format(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11]))

def strikes():
    strikes = input("Strikes: ")
    cursor.execute("SELECT * from ufc_stats_table WHERE strikes = %s;", (strikes,))
    results = cursor.fetchall()
    for item in results:
        print("""
First name: {}
Last name: {}
Fights: {}
Strikes: {}
Strike accuracy: {}
Takedown: {}
Takedown accuracy: {}
Knockdowns: {}
Passes: {}
Reversals: {}
Submissions: {}
""".format(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11]))

def strike_accuracy():
    strike_accuracy = input("Strike accuracy: ")
    cursor.execute("SELECT * from ufc_stats_table WHERE strike_accuracy = %s;", (strike_accuracy,))
    results = cursor.fetchall()
    for item in results:
        print("""
First name: {}
Last name: {}
Fights: {}
Strikes: {}
Strike accuracy: {}
Takedown: {}
Takedown accuracy: {}
Knockdowns: {}
Passes: {}
Reversals: {}
Submissions: {}
""".format(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11]))

def takedowns():
    takedowns = input("Takedowns: ")
    cursor.execute("SELECT * from ufc_stats_table WHERE takedowns = %s;", (takedowns,))
    results = cursor.fetchall()
    for item in results:
        print("""
First name: {}
Last name: {}
Fights: {}
Strikes: {}
Strike accuracy: {}
Takedown: {}
Takedown accuracy: {}
Knockdowns: {}
Passes: {}
Reversals: {}
Submissions: {}
""".format(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11]))

def takedown_accuracy():
    takedown_accuracy = input("Takedown accuracy: ")
    cursor.execute("SELECT * from ufc_stats_table WHERE takedown_accuracy = %s;", (takedown_accuracy,))
    results = cursor.fetchall()
    for item in results:
        print("""
First name: {}
Last name: {}
Fights: {}
Strikes: {}
Strike accuracy: {}
Takedown: {}
Takedown accuracy: {}
Knockdowns: {}
Passes: {}
Reversals: {}
Submissions: {}
""".format(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11]))

def knockdowns():
    knockdowns = input("Knockdowns: ")
    cursor.execute("SELECT * from ufc_stats_table WHERE knockdowns = %s;", (knockdowns,))
    results = cursor.fetchall()
    for item in results:
        print("""
First name: {}
Last name: {}
Fights: {}
Strikes: {}
Strike accuracy: {}
Takedown: {}
Takedown accuracy: {}
Knockdowns: {}
Passes: {}
Reversals: {}
Submissions: {}
""".format(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11]))

def passes():
    passes = input("Passes: ")
    cursor.execute("SELECT * from ufc_stats_table WHERE passes = %s;", (passes,))
    results = cursor.fetchall()
    for item in results:
        print("""
First name: {}
Last name: {}
Fights: {}
Strikes: {}
Strike accuracy: {}
Takedown: {}
Takedown accuracy: {}
Knockdowns: {}
Passes: {}
Reversals: {}
Submissions: {}
""".format(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11]))

def reversals():
    reversals = input("Reversals: ")
    cursor.execute("SELECT * from ufc_stats_table WHERE reversals = %s;", (reversals,))
    results = cursor.fetchall()
    for item in results:
        print("""
First name: {}
Last name: {}
Fights: {}
Strikes: {}
Strike accuracy: {}
Takedown: {}
Takedown accuracy: {}
Knockdowns: {}
Passes: {}
Reversals: {}
Submissions: {}
""".format(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11]))

def submissions():
    submissions = input("Submissions: ")
    cursor.execute("SELECT * from ufc_stats_table WHERE submissions = %s;", (submissions,))
    results = cursor.fetchall()
    for item in results:
        print("""
First name: {}
Last name: {}
Fights: {}
Strikes: {}
Strike accuracy: {}
Takedown: {}
Takedown accuracy: {}
Knockdowns: {}
Passes: {}
Reversals: {}
Submissions: {}
""".format(item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11]))

def help_initials():
    print("""
 Type the [letter(s)] in the bracket to search by that criteria:
 [fn] first name
 [ln] last name
 [f] fights
 [s] strikes
 [sa] strike accuracy
 [t] takedowns
 [ta] takedown accuracy
 [k] knockdowns
 [p] passes
 [r] reversals
 [su] submissions
         """)

def create_new_data():
    print("Follow the prompts below to create a new player data row.")
    new_id = 11
    new_fn = input("Fighter first name: ").upper()
    new_ln = input("Fighter last name: ").upper()
    new_fights = input("Number of fights: ")
    new_strikes = input("Number of strikes: ")
    new_strike_acc = input("Strike accuracy: ")
    new_takedowns = input("Number of takedowns: ")
    new_takedown_acc = input("Takedown accuracy: ")
    new_knockdowns = input("Number of knockdowns: ")
    new_passes = input("Number of passes: ")
    new_reversals = input("Number of reversals: ")
    new_submissions = input("Number of submissions: ")

    cursor.execute("SELECT * FROM ufc_stats_table;")
    results = cursor.fetchall()
    for row in results:
        if new_id == row[0]:
            new_id += 1

    cursor.execute("INSERT INTO ufc_stats_table VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    (new_id,new_fn,new_ln,new_fights,new_strikes,new_strike_acc,new_takedowns,new_takedown_acc,new_knockdowns,new_passes,new_reversals,new_submissions))
    connection.commit()

print("Welcome to a UFC All Weights Database! Here, you can look up stats of different fighters.\n")

while True:
    look_up = input("""
Which criteria would you like to look up?
Type 'h' for a list of criteria, 'c' to create new data row, or 'q' to quit.
>>> """).lower()
    if look_up == 'h':
        help_initials()
    elif look_up == 'fn':
        first_name()
    elif look_up == 'ln':
        last_name()
    elif look_up == 'f':
        fights()
    elif look_up == 's':
        strikes()
    elif look_up == 'sa':
        strike_accuracy()
    elif look_up == 't':
        takedowns()
    elif look_up == 'ta':
        takedown_accuracy()
    elif look_up == 'k':
        knockdowns()
    elif look_up == 'p':
        passes()
    elif look_up == 'r':
        reversals()
    elif look_up == 'su':
        submissions()
    elif look_up.lower() == 'c':
        create_new_data()
    elif look_up.lower() == 'q':
        print("Goodbye.")
        sys.exit()
    else:
        print("Please input an appropriate command.")

connection.commit()
cursor.close()
connection.close()
