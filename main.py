import psycopg2
import os
db_pass = os.getenv('DB_PASS')
conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password=db_pass,
                        port="5432")
print(conn)
