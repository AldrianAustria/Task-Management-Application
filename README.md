# Task-Management-Application
A CLI based python task management application.

## Database Configuration:
Create a schema named _task_ with the following table configurations:

__task_id : INT__ _(Primary Key, Not Null, Auto-Increment)___
__title : VARCHAR____
__description : VARCHAR____
__due : DATETIME____
__priority : VARCHAR____
__status : VARCHAR____
__creation_time : DATETIME____

## Setup guide:
1. Create a venv and activate it to isolate the program to the global libraries.
2. Install the dependencies in the requirements.txt
3. Configure the db_access.cfg that corresponds to your MySQL server credentials.
4. Run the program and enjoy! :)

