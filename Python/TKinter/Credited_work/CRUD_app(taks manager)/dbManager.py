import sqlite3 as sql

class DataBaseManager:
    def __init__(self):
        self.conn = sql.connect('tasks.db')
        self.create_table()
    
    
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT NOT NULL,
            status TEXT NOT NULL,
            creation_date TEXT NOT NULL,
            due_date TEXT NOT NULL,
            completion_date TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()
    
    def create(self, title, description, priority, status, creation_date, due_date, completion_date):
        query = "INSERT INTO tasks (title, description, priority, status, creation_date, due_date, completion_date) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.conn.execute(query, (title, description, priority, status, creation_date, due_date, completion_date))
        self.conn.commit()
    
    def read_all(self):
        query = "SELECT * FROM tasks"
        return self.conn.execute(query).fetchall()
    
    def update(self, record_id, title, description, priority, status, creation_date, due_date, completion_date):
        query = "UPDATE tasks SET (title, description, priority, status, creation_date, due_date, completion_date) VALUES (?, ?, ?, ?, ?, ?, ?) WHERE id = ?"
        self.conn.execute(query, (title, description, priority, status, creation_date, due_date, completion_date, record_id))
        self.conn.commit()
        
    def delete(self, record_id):
        query = "DELETE FROM tasks WHERE id = ?"
        self.conn.execute(query, (record_id,))
        self.conn.commit()