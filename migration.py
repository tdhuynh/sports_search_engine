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
    fights SMALLINT,
    strikes SMALLINT,
    strike_accuracy NUMERIC(3,3),
    takedowns SMALLINT,
    takedown_accuracy NUMERIC(3,3),
    knockdowns SMALLINT,
    passes SMALLINT,
    reversals SMALLINT,
    submissions SMALLINT
);
"""
cursor.execute(create_table_command)

with open('stats.csv') as file:
    contents = list(csv.reader(file))
for row in contents:
    cursor.execute("INSERT INTO ufc_stats_table VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (row[:13]))
connection.commit()

cursor.close()
connection.close()
