# Version 1.2
from time import sleep
import sqlite3, os

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

def clear_screen():
    os.system('cls')

# Création de la table si elle n'existe pas déjà
conn = sqlite3.connect('xpuser.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (name TEXT UNIQUE, password TEXT, current_level INTEGER, xp_needed INTEGER, xp INTEGER)')
conn.commit()

if __name__ == '__main__': # Boucle principale du programme
    clear_screen()
    while True: # Connexion ou création d'un compte utilisateur
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        user_info = get_user_xp_info(name, password)
        if user_info:
            current_level, xp_needed, xp = user_info
            print("Welcome back!")
        else:
            current_level, xp_needed, xp = 0, 200, 0
            try:
                c.execute('INSERT INTO users (name,password, current_level, xp_needed, xp) VALUES (?, ?, ?, ?, ?)', (name, password, current_level, xp_needed, xp))
                conn.commit()
                conn.close()
                print("New account created!")
                sleep(2)
            except sqlite3.IntegrityError:
                clear_screen()
                print(f"`{name}` already exists or you used the wrong password, please try again.")
                continue
        while True: # Boucle pour interagir avec l'utilisateur
            clear_screen()
            choice = input("1. XP info | 2. XP up\nWhat do you want to do: \x1b[?25l")
            if choice.lower() == "1": # Affichage d'informations sur l'expérience de l'utilisateur
                clear_screen()
                while True:
                    clear_screen()
                    try:
                        level = int(input('What level do you want to know the xp ? level '))
                        if level <= current_level:
                            print(f"You're already level \x1b[1m\x1b[38;5;{level + 1 % 256}mlevel {level}\x1b[0m.")
                        else:
                            xp_required = xp_needed * 2**(level-current_level-1) - xp
                            print(f"\nTo reach \x1b[1m\x1b[38;5;{level + 1 % 256}mlevel {level}\x1b[0m, you need \x1b[1;32m{xp_required}\x1b[0m +XP.\n")
                        os.system("pause>null")
                    except ValueError:
                        print("Please enter a valid integer for the level.")
                        os.system("pause>null")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        os.system("pause>null")
            elif choice.lower() == "2": # Permet à l'utilisateur de gagner de l'XP
                clear_screen()
                print("\033[1m\033[91mWARNING:\033[0m If the number is too high, it may crash.")
                while True:
                    try:
                        xp += int(input("How many XP do you want to gain: "))
                        clear_screen()
                        while xp >= xp_needed:
                            current_level += 1
                            xp, xp_needed = xp - xp_needed, xp_needed * 2
                            print(f"\x1b[1m\x1b[32mCongratulations\x1b[0m, you've reached \x1b[1m\x1b[38;5;{current_level - 1 % 256}mLevel {current_level}\x1b[0m!\n")
                        update_user(name, current_level, xp_needed, xp)
                        BOLD = '\x1b[1m\x1b'
                        RESET = '\x1b[0m'
                        GREEN = '\x1b[1;32m'
                        print(f"{BOLD}[38;5;{current_level - 1 % 256}mLevel {current_level}{RESET} \x1b[38;5;41m{'━'*int((xp / xp_needed) * 40)}{RESET}\x1b[38;5;8m╺{'━'*(40-1 - int((xp / xp_needed) * 40))}{RESET} {GREEN}{xp}{RESET}/{GREEN}{xp_needed} XP{RESET}\n{GREEN}{xp_needed - xp} XP{RESET} before reaching {BOLD}[38;5;{current_level % 256}mLevel {current_level + 1}{RESET}.\n")
                    except ValueError:
                        print("Please enter a valid integer for the XP.")
                        continue
            else:...
