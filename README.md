# ICPC Database Management System

## Overview
This Python script implements an ICPC Database Management System allowing admins to interact with a MySQL database. 

## Prerequisites
- Python 3.x
- MySQL Server
- Required Python packages: `subprocess`, `pymysql`, `prettytable`

## Setup
1. Install the required Python packages:
    ```
    pip install pymysql prettytable
    ```

2. Update the `settings.py` file with your MySQL server connection details.

## Usage
1. Run the script:
    ```
    python3 main.py
    ```

2. You will be prompted to enter your MySQL server credentials. Upon successful connection, you can choose from various categories and perform actions within each category.

3. To exit the program, choose option 4.

## Structure
- `main.py`: The main script containing the interactive loop for user input.
- `settings.py`: Configuration file storing MySQL server connection details.
- `queries.py`: File containing SQL queries and query-related functions.
- `general.py`: General utility functions.

## main.py

### Importing Libraries:

- **subprocess:** Used for making system calls, here for clearing the terminal screen.
- **pymysql:** A MySQL database connector for Python.
- **PrettyTable:** A library for creating ASCII tables.
- **general:** Contains general utility functions.
- **queries:** Contains SQL queries.
- **settings:** Initializes global variables.

### Initialization and Connection to the SQL Server:

- The `settings.init()` function is called to initialize settings, presumably including database connection details.
- A connection to the SQL server is attempted, and success or failure is displayed.

### Main User Interaction Loop:

- A `while(1)` loop runs indefinitely until the user chooses to exit (`choice == 4`).
- Inside the loop, the terminal screen is cleared, and a connection to the SQL server is attempted again. If successful, a confirmation message is displayed; otherwise, an error message is shown, and the loop is exited.

### Menu and User Choices:

- The script then displays categories (related to database operations) using `show_categories()`.
- The user is prompted to enter a choice.
- If the choice is to exit (`choice == 4`), the loop breaks; otherwise, it proceeds to show options related to the chosen category.

### Handling Sub-Choices:

- The script displays options based on the user's initial category choice.
- The user is prompted to enter a sub-choice.
- The `dispatch` function is called with the user's main and sub-choices to perform sql operations.

### Exception Handling:

- Exceptions from `pymysql.Error`, are caught, and appropriate error messages are displayed if there are issues with SQL queries or the database connection.

### User Interaction Continuation:

- After performing the chosen operation, the user is prompted to press any key to continue. This provides a pause in the execution, allowing the user to read messages or results before the next iteration of the loop.

## general.py

### Menu and Options Display:

- The script defines functions to display categories and corresponding options based on user choices.
- Categories include Retrieval, Modification, Analysis, and Exit.

### User Interaction and Dispatcher:

- The `dispatch` function is called based on user choices to execute specific operations.
- The script handles retrieval, modification, and analysis categories separately.

### Retrieval Operations:

- For Retrieval, various options are provided, such as retrieving participants in a team, problems set by an author, and more.
- User input is collected for each operation, and corresponding functions from the `queries` module are called.

### Modification Operations:

- For Modification, options include adding submissions, adding test cases, updating test cases, updating scores, disqualifying teams, and removing low-rated teams.
- User input is collected for each operation, and corresponding functions from the `queries` module are called.

### Analysis Operations:

- For Analysis, options include displaying the average penalty for a problem, generating a rank list of teams, and retrieving the acceptance rate of problems by an author.
- User input is collected for each operation, and corresponding functions from the `queries` module are called.

## queries.py

- Contains queries for each SQL operation under appropriate functions which take user input as argument.



