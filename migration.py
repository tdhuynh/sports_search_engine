# stats taken from http://www.foxsports.com/ufc/stats?weightclass=11&category=BASIC
import csv
import psycopg2

connection = psycopg2.connect("dbname=ufc_allweights_stats user=ufc_allweights_stats")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS ufc_stats_table;")

create_table_command = """
CREATE TABLE ufc_stats_table (
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    strikes NUMERIC(4),
    strike_accuracy NUMERIC(4,4),
    takedowns NUMERIC(2),
    takedown_accuracy NUMERIC(4,4),
    knockdowns NUMERIC(1),
    passes NUMERIC(2),
    reversals NUMERIC(1),
    submissions NUMERIC(1)
);
"""
cursor.execute(create_table_command)

with open('stats.csv') as file:
    contents = list(csv.reader(file))
    for row in contents:
        cursor.execute("INSERT INTO ufc_stats_table VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],))


# cursor.execute("INSERT INTO ufc_stats_table VALUES (1, 'NATE DIAZ', '1926', '.538', '17', '.262', '3', '15', '6', '9')")



connection.commit()


cursor.close()
connection.close()
