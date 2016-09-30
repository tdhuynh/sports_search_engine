import psycopg2

connection = psycopg2.connect("dbname=ufc_allweights_stats user=ufc_allweights_stats")
cursor = connection.cursor()

def first_name():
    if look_up == 'fn':
        first_name = input("First name: ").upper()
        cursor.execute("SELECT * from ufc_stats_table WHERE first_name = %s;", (first_name,))

def last_name():
    if look_up == 'ln':
        last_name = input("Last name: ").upper()
        cursor.execute("SELECT * from ufc_stats_table WHERE last_name = %s;", (last_name,))

def fights():
    if look_up == 'f':
        fights = input("Fights: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE fights = %s;", (fights,))

def strikes():
    if look_up == 's':
        strikes = input("Strikes: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE strikes = %s;", (strikes,))

def strike_accuracy():
    if look_up == 'sa':
        strike_accuracy = input("Strike accuracy: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE strike_accuracy = %s;", (strike_accuracy,))

def takedowns():
    if look_up == 't':
        takedowns = input("Takedowns: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE takedowns = %s;", (takedowns,))

def takedown_accuracy():
    if look_up == 'ta':
        takedown_accuracy = input("Takedown accuracy: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE takedown_accuracy = %s;", (takedown_accuracy,))

def knockdowns():
    if look_up == 'k':
        knockdowns = input("Knockdowns: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE knockdowns = %s;", (knockdowns,))

def passes():
    if look_up == 'p':
        passes = input("Passes: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE passes = %s;", (passes,))

def reversals():
    if look_up == 'r':
        reversals = input("Reversals: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE reversals = %s;", (reversals,))

def submissions():
    if look_up == 'su':
        submissions = input("Submissions: ")
        cursor.execute("SELECT * from ufc_stats_table WHERE submissions = %s;", (submissions,))

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
    results = cursor.fetchall()
    print(results)

print("Welcome to a Sports Database!")

look_up_list = ['fn', 'ln', 'f', 's', 'sa', 't', 'ta', 'k', 'p', 'r', 'su']
while True:
    look_up = input("""How would you like to look up a fighter's stats?\n
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
                       [su] submissions\n>>> """)


    if look_up in look_up_list:
        categories()
    else:
        print("Please type a correct command.")






connection.commit()

cursor.close()
connection.close()
