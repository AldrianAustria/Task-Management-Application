class Tasks:
    """Simple data-access class for the tasks table.

    Provides create, read, update and delete operations to
    MySQL connection.  The constructor takes a live ``pymysql``
    ``Connection`` object, which is used to obtain cursors for
    executing statements.
    """

    def __init__(self, db):
        """Initialize with a pymysql Connection object."""
        self.db = db

    def create_task(self, title, description, due_date, priority, status, time_stamp):
        """Insert a new row into the tasks table."""
        query = "INSERT INTO tasks (title, description, due, priority, status, creation_time) VALUES (%s, %s, %s, %s, %s, %s)"
        with self.db.cursor() as cursor:
            cursor.execute(query, (title, description, due_date, priority, status, time_stamp))
        self.db.commit()

    def get_tasks(self):
        """Return all rows from the tasks table."""
        query = "SELECT * FROM tasks"
        with self.db.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def update_task(self, task_id, title=None, description=None, priority=None, status=None):
        """Modify one or more fields of an existing task by id."""
        with self.db.cursor() as cursor:
            if title:
                query = "UPDATE tasks SET title = %s WHERE task_id = %s"
                cursor.execute(query, (title, task_id))
            if description:
                query = "UPDATE tasks SET description = %s WHERE task_id = %s"
                cursor.execute(query, (description, task_id))
            if priority:
                query = "UPDATE tasks SET priority = %s WHERE task_id = %s"
                cursor.execute(query, (priority, task_id))
            if status:
                query = "UPDATE tasks SET status = %s WHERE task_id = %s"
                cursor.execute(query, (status, task_id))
        self.db.commit()

    def delete_task(self, task_id):
        """Delete a task by its ID."""
        query = "DELETE FROM tasks WHERE task_id = %s"
        with self.db.cursor() as cursor:
            cursor.execute(query, (task_id,))
        self.db.commit()