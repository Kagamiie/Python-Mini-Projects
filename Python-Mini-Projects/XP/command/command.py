from command.db import update_user
import const, os

def xpuper(name, current_level, xp_needed, xp):
    print(f"{const.CLS}{const.WARNING} If the number is too high, it may crash.")
    while True:
        try:
            new_xp = int(input(f"{const.INTEROGATION} How many XP do you want to gain: "))
            if new_xp < 0 or xp + new_xp < 0:
                raise ValueError
            xp += new_xp
            while xp >= xp_needed:
                current_level += 1
                xp, xp_needed = xp - xp_needed, xp_needed * 2
                #print(f"{const.SUCCESS}{const.BOLD}{const.GREEN}Congratulations{const.RESET}, you've reached {const.BOLD}[38;5;{current_level % 256}mLevel {current_level + 1}{const.RESET}!")
                update_user(name, current_level, xp_needed, xp)
            percent = int(xp / xp_needed * 40)
            print(f"{const.CLS}{const.BOLD}[38;5;{current_level - 1 % 256}mLevel {current_level}{const.RESET} \x1b[38;5;41m{'━'*percent}{const.RESET}\x1b[38;5;8m╺{'━'*(40-1 - percent)}{const.RESET} {const.GREEN}{xp}{const.RESET}/{const.GREEN}{xp_needed} XP{const.RESET}\n{const.GREEN}{xp_needed - xp} XP{const.RESET} before reaching {const.BOLD}[38;5;{current_level + 1 % 256}mLevel {current_level + 1}{const.RESET}.\n")
        except ValueError:
            print(f"{const.CLS}{const.WARNING} Please enter a valid whole number for the XP.")

def xpinf(current_level, xp_needed, xp):
    while True:
        try:
            percent = int((xp / xp_needed) * 40)
            print(f"{const.CLS}{const.BOLD}[38;5;{current_level % 256}mLevel {current_level}{const.RESET} \x1b[38;5;41m{'━'*percent}{const.RESET}\x1b[38;5;8m╺{'━'*(40-1 - percent)}{const.RESET} {const.GREEN}{xp}{const.RESET}/{const.GREEN}{xp_needed} XP{const.RESET}")
            level = int(input(f'{const.INTEROGATION} What level do you want to know the xp ? level '))
            if level <= current_level:
                print(f"\nYou're already level {const.BOLD}[38;5;{level + 1 % 256}mlevel {level}{const.RESET}.")
            else:
                xp_required = xp_needed * (2**(level-current_level-1)) - xp
                print(f"\nTo reach {const.BOLD}[38;5;{level + 2 % 256}mlevel {level}{const.RESET}, you need {const.GREEN}{xp_required}{const.RESET} +XP.\n")
            os.system('pause>null')
        except ValueError:
            print(f"{const.WARNING} Please enter a valid whole number for the level.\n")
            os.system('pause>null')
        except Exception as e:
            print(f"{const.WARNING} An error occurred: {e}\n")
            os.system('pause>null')