import sqlite3
from datetime import datetime

conn = sqlite3.connect('sre_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS simulations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    type TEXT,
    parameters TEXT,
    results TEXT
)
''')
conn.commit()

def save_result(sim_type, params, results):
    timestamp = datetime.now().isoformat()
    cursor.execute('''
    INSERT INTO simulations (timestamp, type, parameters, results)
    VALUES (?, ?, ?, ?)
    ''', (timestamp, sim_type, str(params), str(results)))
    conn.commit()

def query_results(sim_type=None):
    if sim_type:
        cursor.execute('SELECT * FROM simulations WHERE type = ?', (sim_type,))
    else:
        cursor.execute('SELECT * FROM simulations')
    return cursor.fetchall()
