# Needed imports
import sqlite3, os

# Local py file
from command.command import xpuper, xpinf
from command.db import get_user_xp_info, create_user

def cls():
    os.system('cls')

conn = sqlite3.connect('xpuser.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (name TEXT UNIQUE, password TEXT, current_level INTEGER, xp_needed INTEGER, xp INTEGER)')
conn.commit()

if __name__ == '__main__': # Boucle principale du programme
    cls()
    while True: # Connexion ou création d'un compte utilisateur
        name = input("Enter your name: \x1b[?25l")
        password = input("Enter your password: \x1b[?25l")

        user_info = get_user_xp_info(name, password)
        if user_info:
            current_level, xp_needed, xp = user_info
        else:
            current_level, xp_needed, xp = 0, 200, 0
            try:
                create_user(name, password, current_level,xp_needed, xp)
                print(f"\n{const.SUCCESS} New account created!\x1b[?25l")
                sleep(2)
            except sqlite3.IntegrityError:
                cls()
                print(f"{const.WARNING} `{name}` already exists or you used the wrong password, please try again.\n\x1b[?25l")
                continue
            
        while True:
            cls()
            choice = input(f"1. XP info | 2. XP up\n{const.INTEROGATION}  What do you want to do: \x1b[?25l")
            
            if choice == "1": 
                xpinf(current_level, xp_needed, xp)
            elif choice == "2":
                xpuper(name, current_level, xp_needed, xp)
        else:...