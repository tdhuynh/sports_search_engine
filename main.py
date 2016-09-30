import psycopg2

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
         [fn] first name\n
         [ln] last name\n
         [f] fights\n
         [s] strikes\n
         [sa] strike accuracy\n
         [t] takedowns\n
         [ta] takedown accuracy\n
         [k] knockdowns\n
         [p] passes\n
         [r] reversals\n
         [su] submissions\n
         """)

def categories():
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


print("Welcome to a Sports Database!")

look_up_list = ['fn', 'ln', 'f', 's', 'sa', 't', 'ta', 'k', 'p', 'r', 'su', 'h']
while True:
    look_up = input("How would you like to look up a fighter's stats? Type 'H' for help.\n>>> ")

    if look_up.lower() in look_up_list:
        categories()
    else:
        print("Please type a correct command.")






connection.commit()

cursor.close()
connection.close()
