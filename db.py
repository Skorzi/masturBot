import sqlite3

connect = sqlite3.connect("drochunsBase.db", check_same_thread=False)
cursor = connect.cursor()

def create_table():
    cursor.execute(""" CREATE TABLE IF NOT EXISTS drochunsBase(
        user_id INTEGER PRIMARY KEY,
        date TEXT,
        date_time TEXT
    ) """)

    connect.commit()

def add_to_db(user_id, date, date_time):
    users_list = [user_id, date, date_time]
    cursor.execute("INSERT INTO drochunsBase VALUES(?,?,?);", users_list)
    connect.commit()

def search_db():
    cursor.execute("SELECT * FROM drochunsBase")
    all_results = cursor.fetchall()
    return all_results

def delete_from_db(user_id):
    cursor.execute("DELETE FROM drochunsBase WHERE user_id == ?", (user_id,))
    connect.commit()

def delete_all_db():
    cursor.execute("DROP TABLE drochunsBase")
    connect.commit()

def update_table_db(user_id, date, date_time):
    cursor.execute("UPDATE drochunsBase SET date_time == ? WHERE user_id == ?", (date_time, user_id))
    cursor.execute("UPDATE drochunsBase SET date = ? WHERE user_id = ?", (date, user_id))
    connect.commit()

