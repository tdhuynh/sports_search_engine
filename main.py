import psycopg2
import sys

# manually start:  pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

connection = psycopg2.connect("dbname=ufc_allweights_stats user=ufc_allweights_stats")
cursor = connection.cursor()

def first_name():
    if look_up == 'fn':
        first_name = input("First name: ").upper()
        cursor.execute("SELECT * from ufc_stats_table WHERE first_name = %s;", (first_name,))
        results = cursor.fetchall()
        print(results)

def last_name():
    if look_up == 'ln':
        last_name = input("Last name: ").upper()
        cursor.execute("SELECT * from ufc_stats_table WHERE last_name = %s;", (last_name,))
        results = cursor.fetchall()
        print(results)

def fights():
    if look_up == 'f':
        fights = input("Fights: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE fights = %s;", (fights,))
        results = cursor.fetchall()
        print(results)

def strikes():
    if look_up == 's':
        strikes = input("Strikes: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE strikes = %s;", (strikes,))
        results = cursor.fetchall()
        print(results)

def strike_accuracy():
    if look_up == 'sa':
        strike_accuracy = input("Strike accuracy: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE strike_accuracy = %s;", (strike_accuracy,))
        results = cursor.fetchall()
        print(results)

def takedowns():
    if look_up == 't':
        takedowns = input("Takedowns: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE takedowns = %s;", (takedowns,))
        results = cursor.fetchall()
        print(results)

def takedown_accuracy():
    if look_up == 'ta':
        takedown_accuracy = input("Takedown accuracy: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE takedown_accuracy = %s;", (takedown_accuracy,))
        results = cursor.fetchall()
        print(results)

def knockdowns():
    if look_up == 'k':
        knockdowns = input("Knockdowns: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE knockdowns = %s;", (knockdowns,))
        results = cursor.fetchall()
        print(results)

def passes():
    if look_up == 'p':
        passes = input("Passes: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE passes = %s;", (passes,))
        results = cursor.fetchall()
        print(results)

def reversals():
    if look_up == 'r':
        reversals = input("Reversals: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE reversals = %s;", (reversals,))
        results = cursor.fetchall()
        print(results)

def submissions():
    if look_up == 'su':
        submissions = input("Submissions: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE submissions = %s;", (submissions,))
        results = cursor.fetchall()
        print(results)

def help_initials():
    if look_up == 'h':
        print("""
         Type the letter(s) in the bracket to search by that criteria:
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

def stat_categories():
    first_name()
    last_name()
    fights()
    strikes()
    strike_accuracy()
    takedowns()
    takedown_accuracy()
    knockdowns()
    passes()
    reversals()
    submissions()
    help_initials()

print("Welcome to a UFC All Weights Database! Here, you can look up stats of different fighters.\n")

look_up_list = ['fn', 'ln', 'f', 's', 'sa', 't', 'ta', 'k', 'p', 'r', 'su', 'h']
while True:
    look_up = input("What would you like to do? Type 'h' for a list of commands, 'c' to create new data row, or 'q' to quit.\n>>> ").lower()
    if look_up in look_up_list:
        stat_categories()
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
