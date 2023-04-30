#Version 1.0
import sqlite3, os

conn = sqlite3.connect('xpuser.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, current_level INTEGER, xp_needed INTEGER, xp INTEGER)')
conn.commit()

def clear_screen():
    os.system("cls")

def get_user_xp_info(name):
    c.execute('SELECT current_level, xp_needed, xp FROM users WHERE name = ?', (name,))
    row = c.fetchone()
    if row:
        return row
    else:
        return None

def set_user_xp_info(name, current_level, xp_needed, xp):
    c.execute('INSERT OR REPLACE INTO users (name, current_level, xp_needed, xp) VALUES (?, ?, ?, ?)', (name, current_level, xp_needed, xp))
    conn.commit()

if __name__ == '__main__':
    clear_screen()
    name = input("Enter your name: ")
    user_info = get_user_xp_info(name)
    if user_info:
        current_level, xp_needed, xp = user_info
    else:
        current_level, xp_needed, xp = 0, 200, 0
    while True:
        clear_screen()
        choice = input("1. XP info | 2. XP up\nWhat do you want to do: \x1b[?25l")
        
        if choice.lower() == "1":
            clear_screen()
            while True:
                clear_screen()
                try:
                    level = int(input('What level do you want to know the xp ? level '))
                    if level <= current_level:
                        print(f"You're already level \x1b[1m\x1b[38;5;{level + 1 % 256}mlevel {level}\x1b[0m.")
                        os.system("pause>null")
                    else:
                        xp_needed_for_level = xp_needed * 2**(level-current_level-1)
                        xp_required = xp_needed_for_level - xp
                        print(f"\nTo reach \x1b[1m\x1b[38;5;{level + 1 % 256}mlevel {level}\x1b[0m, you need \x1b[1;32m{xp_required}\x1b[0m +XP.\n")                
                        os.system("pause>null")
                except ValueError:
                    print("Please enter a valid integer for the level.")
                    continue
                except Exception as e:
                    print(f"An error occurred: {e}")
                    continue

        elif choice.lower() == "2":
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
                    set_user_xp_info(name, current_level, xp_needed, xp)
                    print(f"\x1b[1m\x1b[38;5;{current_level - 1 % 256}mLevel {current_level}\x1b[0m \x1b[38;5;41m{'━'*int((xp / xp_needed) * 40)}\x1b[38;5;8m╺{'━'*(40-1 - int((xp / xp_needed) * 40))}\x1b[0m \x1b[1;32m{xp}\x1b[0m/\x1b[1;32m{xp_needed} XP\x1b[0m",f"\n\x1b[1;32m{xp_needed - xp} XP\x1b[0m before reaching \x1b[1m\x1b[38;5;{current_level % 256}mLevel {current_level + 1}\x1b[0m.\n")
                    break
                except ValueError:
                    print("Please enter a valid integer for the XP.")
                    continue
                except Exception as e:
                    print(f"An error occurred: {e}")
                    continue
        else: ...
