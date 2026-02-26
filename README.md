# Task-Management-Application
A CLI based python task management application.

## Database Configuration:
Create a schema named _task_ with the following table configurations:

__task_id : INT__ _(Primary Key, Not Null, Auto-Increment)_<br>
__title : VARCHAR__<br>
__description : VARCHAR__<br>
__due : DATETIME__<br>
__priority : VARCHAR__<br>
__status : VARCHAR__<br>
__creation_time : DATETIME__<br>

## Setup guide:
1. Create a venv and activate it to isolate the program to the global libraries.
2. Install the dependencies in the requirements.txt
3. Configure the db_access.cfg that corresponds to your MySQL server credentials.
4. Run the program and enjoy! :)


