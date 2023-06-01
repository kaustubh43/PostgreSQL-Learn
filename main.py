import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="",
                        port="5432")

