# SQL COMMANDS

# CRETATE DATABASE todoapp;
# USE todoapp;
# CREATE TABLE task (
#     id INT NOT NULL AUTO_INCREMENT,
#     description VARCHAR(255) NOT NULL,
#     state VARCHAR(255) NOT NULL,
#     priority INT NOT NULL,
#     PRIMARY KEY (id)
# );

import mysql.connector

def get_connection():
    connect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'todoapp'
    )
    return connect

connection = get_connection()

def select_all_task():
    cursor = connection.cursor(dictionary=True) # type: ignore
    sql = "SELECT * FROM task;"
    cursor.execute(sql)
    tasks = cursor.fetchall()
    connection.close()
    return tasks

def insert_task(task):
    cursor = connection.cursor()
    sql = "INSERT INTO task (description, state, priority) VALUES (%s, %s, %s);"
    cursor.execute(sql, [task["description"], task["estoque"], task["priority"]])
    connection.commit()
    connection.close()

def delete_task(id):
    cursor = connection.cursor()
    sql = "DELETE FROM task WHERE id = %s;"
    cursor.execute(sql, [id])
    connection.commit()
    connection.close()

def update_task(task, id):
    cursor = connection.cursor()
    sql = "UPDATE task SET description = %s, state = %s, priority = %s,  WHERE id = %s;"
    cursor.execute(sql, [task["descricao"], task["estoque"], task["priority"],id])
    connection.commit()
    connection.close()

def select_task_low_priority():
    cursor = connection.cursor()
    sql = "SELECT * FROM task WHERE priority = 1;"
    cursor.execute(sql)
    connection.commit()
    connection.close()

def select_task_high_priority():
    cursor = connection.cursor()
    sql = "SELECT * FROM task WHERE priority = 5;"
    cursor.execute(sql)
    connection.commit()
    connection.close()

def select_task_priority(priority):
    cursor = connection.cursor()
    sql = "SELECT * FROM task WHERE priority = %s;"
    cursor.execute(sql, priority)
    connection.commit()
    connection.close()

def select_task_todo_state(state):
    cursor = connection.cursor()
    sql = "SELECT * FROM task WHERE state = %s;"
    cursor.execute(sql, state)
    connection.commit()
    connection.close()

def select_task_doing_state(state):
    cursor = connection.cursor()
    sql = "SELECT * FROM task WHERE state = %s;"
    cursor.execute(sql, state)
    connection.commit()
    connection.close()

def select_task_done_state(state):
    cursor = connection.cursor()
    sql = "SELECT * FROM task WHERE state = %s;"
    cursor.execute(sql, state)
    connection.commit()
    connection.close()

def select_task_state_priority(state, priority):
    cursor = connection.cursor()
    sql = "SELECT * FROM task WHERE state = %s AND priority = %s;"
    cursor.execute(sql, state, priority)
    connection.commit()
    connection.close()