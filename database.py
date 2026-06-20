import sqlite3

conn = sqlite3.connect("data/bot.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS subscriptions(
    user_id INTEGER,
    artist TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS releases(
    artist TEXT,
    release_id TEXT
)
''')

conn.commit()
