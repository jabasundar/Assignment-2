import sqlite3
import pandas as pd
import os


# project folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# database path
db_path = os.path.join(BASE_DIR, "marketing.db")

# sql file path
sql_path = os.path.join(BASE_DIR, "sql_queries.sql")


# connect database
conn = sqlite3.connect(db_path)


# read sql file
with open(sql_path, "r", encoding="utf-8") as file:
    sql_script = file.read()


# split individual queries
queries = sql_script.split(";")

for i, query in enumerate(queries):

    query = query.strip()

    if query:

        print("\n==============================")
        print("Running Query", i+1)
        print("==============================")

        try:
            result = pd.read_sql(query, conn)

            print(result.head(10))

        except Exception as e:
            print("Error:", e)


conn.close()

print("\nAll SQL queries executed successfully!")