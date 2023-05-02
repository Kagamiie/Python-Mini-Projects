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
