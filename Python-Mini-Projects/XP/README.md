# XP Tracker

The XP tracker is a Python script that allows users to track their experience points (XP) and levels in a simple command-line interface. <br>
The script uses the rich.progress module to display a progress bar during loading, and the os and time modules for various functionalities.<br>

It also use `sqlite3` to all the database stuff, it store all your user's : `level`, `xp`, and `xp_required`. <br>
It'll be stored under the username that you typed when you start the script.

***Please***: note that this code is provided as an educational example only, this code may changed in the futur to be more secured, but it doesn't mean that you can using it. This project should not be used for any personal or professional purposes. This is because the code is not designed with security in mind and could be easily cracked by an attacker. Additionally, as an open source project, it may have vulnerabilities that have not yet been discovered or fixed. Therefore, it is recommended that you use a secure, trusted encryption library for any sensitive data or communication.

## Installation

This tool does not require any installation. Simply download the `var.py` file and run it using Python.
<br>

# Usage

To use the XP tracker, simply run the `var.py` file in your Python environment. The script will display a progress bar that "load" everything. <br>
After the progress bar completes, you will be prompted with a menu that allows you to view your current XP information or gain more XP.

## XP Info
To view your XP information, select option 1 from the menu. <br>
- You will be prompted to enter the level you want to know, and the script will calculate how much XP you need to reach that level. <br>
- The script will also display the amount of XP you need to gain to reach the next level. To go back to the main menu, press y when prompted.

## XP Up
To gain XP, select option 2 from the menu. 
- The script will prompt you to enter the number of levels you want to gain. You can enter any positive integer, but be aware that entering a very large number may cause the script to crash. 
- After entering the number of levels, the script will simulate gaining XP and display your progress towards the next level. When you reach a new level, the script will congratulate you and display your new level and XP progress.

# Dependencies
This script requires the following packages:
- sqlite3 and os 
    - There're both native so you don't need to install anything.


# License
This tool is released under the MIT License. See [LICENSE](https://github.com/Kagamiie/Python-Mini-Projects/blob/afe6d60762ad3e834578d1998c144c06be8ce26d/LICENSE) file for details.

# Contributing
Contributions are welcome! If you find any issues or have any suggestions for improvements, please submit a pull request or open an issue.

<br>
