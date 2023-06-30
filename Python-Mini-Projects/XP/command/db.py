import sqlite3

def create_user(name, password, current_level,xp_needed, xp):
    conn = sqlite3.connect('xpuser.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (name,password, current_level, xp_needed, xp) VALUES (?, ?, ?, ?, ?)', (name, password, current_level, xp_needed, xp))
    conn.commit()
    conn.close()

# Fonctions d'accès et de modification de la base de données
def get_user_xp_info(name, password):
    conn = sqlite3.connect('xpuser.db')
    c = conn.cursor()
    c.execute('SELECT current_level, xp_needed, xp FROM users WHERE name = ? AND password = ?', (name, password))
    user_info = c.fetchone()
    return user_info
    conn.close()

def update_user(name, current_level, xp_needed, xp):
    conn = sqlite3.connect('xpuser.db')
    c = conn.cursor()
    c.execute('UPDATE users SET current_level = ?, xp_needed = ?, xp = ? WHERE name = ?', (current_level, xp_needed, xp, name))
    conn.commit()
    conn.close()