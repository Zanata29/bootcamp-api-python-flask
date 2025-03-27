import sqlite3
import os

def initialize_db():
    db_file = './db/BD_Bootcamp.db'
    if not os.path.exists(db_file):
        open(db_file, 'w').close()
        exec_sql(db_file)

def exec_sql(db_file):
    sql_files_dir = './db/sql'

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    files = ["schema.sql", "populate.sql"]

    for file in files:
        with open(os.path.join(sql_files_dir, file), 'r') as buffer_file:
            sql_script = buffer_file.read()
            cursor.executescript(sql_script)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
