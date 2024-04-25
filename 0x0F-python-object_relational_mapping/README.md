# SQLAlchemy Project

This project contains solutions for several tasks related to SQLAlchemy ORM.

## Description

This project consists of Python scripts that use SQLAlchemy ORM to interact with a MySQL database. It includes solutions for the following tasks:

- **Task 0**: [Get all states](0-select_states.py) - Script to list all states from a database.
- **Task 1**: [Filter states](1-filter_states.py) - Script to list all states starting with the letter 'N'.
- **Task 2**: [Filter states by user input](2-my_filter_states.py) - Script to list all states matching a user input.
- **Task 3**: [SQL Injection...](3-my_safe_filter_states.py) - Script to list all states matching a user input (safe from SQL injection).
- **Task 4**: [Cities by states](4-cities_by_state.py) - Script to list all cities from a database.
- **Task 5**: [All cities by state](5-filter_cities.py) - Script to list all cities of a state.
- **Task 6**: [First state model](model_state.py) - Definition of a State class and an instance Base = declarative_base().
- **Task 7**: [All states via SQLAlchemy](7-model_state_fetch_all.py) - Script to list all State objects from a database.
- **Task 8**: [First state](8-model_state_fetch_first.py) - Script to print the first State object from a database.
- **Task 9**: [Contains 'a'](9-model_state_filter_a.py) - Script to list all State objects containing the letter 'a'.
- **Task 10**: [Get a state](10-model_state_my_get.py) - Script to print the State object with the name passed as an argument.
- **Task 11**: [Add a new state](11-model_state_insert.py) - Script to add a State object to a database.
- **Task 12**: [Update a state](12-model_state_update_id_2.py) - Script to change the name of a State object in a database.
- **Task 13**: [Delete states](13-model_state_delete_a.py) - Script to delete all State objects containing the letter 'a'.
- **Task 14**: [Cities in state](14-model_city_fetch_by_state.py) - Script to print all City objects from a database.

## Installation

1. Clone the repository:

2. Navigate to the project directory:

3. Install the required dependencies:

## Usage

To run each task, execute the corresponding Python script. For example, to run Task 0, use the following command:
python 0-select_states.py <username> <password> <database_name>

Replace `<username>`, `<password>`, and `<database_name>` with your MySQL credentials.
