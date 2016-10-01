import psycopg2
import sys
import csv

# manually start:      pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start


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

def create_user():
    with open(stats.csv, 'a') as write_file:
        contents = csv.writer(write_file)


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



print("Welcome to a UFC All Weights Database! Here, you can look up stats of different fighters.")

look_up_list = ['fn', 'ln', 'f', 's', 'sa', 't', 'ta', 'k', 'p', 'r', 'su']

while True:
    look_up = input("What would you like to do? Type 'h' for a list of commands, 'q' to quit, or 'c' to create a new data row.\n>>> ")
    if look_up.lower() in look_up_list:
        stat_categories()
    elif look_up.lower() == 'h':
        help_initials()
    elif look_up.lower() == 'c':
        pass
    else:
        print("Goodbye.")
        sys.exit()






connection.commit()

cursor.close()
connection.close()
