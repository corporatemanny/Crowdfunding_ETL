import psycopg2
import csv 

connection = psycopg2.connect(
    dbname = 'crowdfunding_etl',
    user= 'treestumpog',
)

cursor = connection.cursor()

with open('Resources/contacts.csv', 'r') as c:
    next(c)
    cursor.copy_from(c, 'contacts', sep=',', columns=('contact_id', 'first_name', 'last_name', 'email'))


connection.commit()

cursor.close()
connection.close()