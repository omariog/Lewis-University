# Author: Omario Gooding
# Date: July 12, 2026
# Description: This program stores and manages personal tasks using SQLite.
# Tier attempted: Base Level

import sqlite3


def create_connection(db_file):
    # Opens the database connection.
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as error:
        print("Connection error:", error)
        return None


def setup_database(conn):
    # Creates the tasks table.
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT DEFAULT 'Medium',
                status TEXT DEFAULT 'Pending',
                due_date TEXT,
                project_id INTEGER
            )
        """)
        conn.commit()
    except sqlite3.Error as error:
        print("Database setup error:", error)


def add_task(conn, title, description, priority, due_date):
    # Adds one task to the database.
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tasks
            (title, description, priority, status, due_date, project_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, description, priority, "Pending", due_date, None))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as error:
        print("Error adding task:", error)
        return None


def get_all_tasks(conn):
    # Gets all tasks.
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks ORDER BY priority, due_date")
        return cursor.fetchall()
    except sqlite3.Error as error:
        print("Error getting tasks:", error)
        return []


def get_tasks_by_status(conn, status):
    # Gets tasks with a certain status.
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM tasks WHERE status = ? ORDER BY priority",
            (status,)
        )
        return cursor.fetchall()
    except sqlite3.Error as error:
        print("Error getting tasks by status:", error)
        return []


def update_task_status(conn, task_id, new_status):
    # Changes the status of a task.
    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            (new_status, task_id)
        )
        conn.commit()

        if cursor.rowcount > 0:
            return True
        else:
            return False
    except sqlite3.Error as error:
        print("Error updating task:", error)
        return False


def delete_task(conn, task_id):
    # Deletes a task using its ID.
    try:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        conn.commit()

        if cursor.rowcount > 0:
            return True
        else:
            return False
    except sqlite3.Error as error:
        print("Error deleting task:", error)
        return False


def display_tasks(tasks):
    # Displays tasks in a table.
    if len(tasks) == 0:
        print("No tasks found.")
        return

    print(f"{'ID':<5}{'Title':<27}{'Priority':<12}{'Status':<15}{'Due Date':<12}")
    print("-" * 71)

    for task in tasks:
        task_id = task[0]
        title = task[1][:25]
        priority = task[3]
        status = task[4]
        due_date = task[5]

        print(
            f"{task_id:<5}"
            f"{title:<27}"
            f"{priority:<12}"
            f"{status:<15}"
            f"{due_date:<12}"
        )


def main():
    # Connect to the database.
    conn = create_connection("tasks.db")

    if conn is None:
        print("Could not open the database.")
        return

    setup_database(conn)

    # Add six sample tasks.
    task1 = add_task(
        conn,
        "Complete database assignment",
        "Finish the SQLite assignment",
        "High",
        "2026-07-15"
    )

    task2 = add_task(
        conn,
        "Prepare presentation",
        "Prepare notes for class",
        "Medium",
        "2026-07-18"
    )

    task3 = add_task(
        conn,
        "Read programming chapter",
        "Read the database chapter",
        "Low",
        "2026-07-14"
    )

    task4 = add_task(
        conn,
        "Study for final exam",
        "Review Python and SQL",
        "High",
        "2026-07-24"
    )

    task5 = add_task(
        conn,
        "Update weekly schedule",
        "Add school and work activities",
        "Medium",
        "2026-07-13"
    )

    task6 = add_task(
        conn,
        "Clean download folder",
        "Remove old files",
        "Low",
        "2026-07-20"
    )

    task_ids = [task1, task2, task3, task4, task5, task6]

    for task_id in task_ids:
        print("Task added with ID:", task_id)

    print("\n=== All Tasks ===")
    display_tasks(get_all_tasks(conn))

    print("\n=== Pending Tasks ===")
    display_tasks(get_tasks_by_status(conn, "Pending"))

    updated = update_task_status(conn, task1, "In Progress")

    if updated:
        print("\nTask status was updated.")
    else:
        print("\nTask was not found.")

    deleted = delete_task(conn, task6)

    if deleted:
        print("Task was deleted.")
    else:
        print("Task was not found.")

    print("\n=== Final Task List ===")
    display_tasks(get_all_tasks(conn))

    conn.close()


if __name__ == "__main__":
    main()
