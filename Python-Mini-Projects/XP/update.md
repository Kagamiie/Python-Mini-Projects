# Update 1.1
## Fixes:

- New SQL statement to add or update user information. This allows adding a new user if it does not already exist in the database instead of recreating an account each time.
- Improved memory management to reduce memory leaks and system instability issues.
- Added new features to make it easier to develop and deploy applications, such as performance monitoring tools and debugging tools.
- Improved system security and reliability.
- Fixed bugs and stability issues.
- Performance optimization to improve response times and application execution speeds.


# Update 1.2
## Fixes:

- Added proper closing of the database connection after executing a query in `get_user_xp_info()` and `update_user()` functions.
- Fixed an issue where the program would crash if the user entered a non-integer value for the XP in the XP up section.
- Fixed an error in the color code of the XP bar that caused it to not display the correct color.
- Added a warning message to the XP up section to warn users about the possibility of crashing the program if they enter a large XP value.
- Improved the clarity of some of the print statements in the program.

# Version 1.3
## Add/New features:

- **Main features**:
    - Improve the readability of the main file, the code for database interactions has been separated into a separate file called `db.py` and `command.py`. Those files contains all of the necessary functions to interact with the database, and the main command of the script.
    - Print a new interface to the main menu, showing : the current version of the script (and the name of the current version), with the name of the procject.
    - Added some new interface ex : [ + ], [ ? ], [ ! ] at the beginning of the print (can be found in the `const.py` file).
<br>
- **`Command.py`**:
    - **XP Upgrade**:
        - Improved readability of code by using constant variables to replace escape sequences.
        - Added input validation to ensure that the user inputs a valid whole number for the XP.
        -  Color scheme for consistency and added more descriptive text for certain print statements.
        - Removed unnecessary use of clearing the screen and replaced it with a constant variable for readability (ANSI code).
        - Added check for negative XP values to prevent errors and crashes.
        <br>
    - **XP Information**:
        - Improved user interface with colored output and progress bar
        - Added a constant module for better code readability
        - Changed function name from xpinf to xp_info for better readability
        - Handled more specific exceptions for better error handling
        - Improved the logic for calculating required XP to reach a certain level
        - Added more informative messages for the user.
        <br>
    - **`db.py`**
        - Put all of the functions related to the database.