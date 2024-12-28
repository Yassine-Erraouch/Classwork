import sqlite3 as sql


class StudentDB:
    def __init__(self):
        self.conn = sql.connect("students.db")
        self.create_table()
        
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            major TEXT NOT NULL)"""
        
        self.conn.execute(query)
        self.conn.commit()
    
    def create(self, name, birth_date, major):
        query = "INSERT INTO students (name, birth_date, major) VALUES (?, ?, ?)"
        self.conn.execute(query, (name, birth_date, major))
        self.conn.commit()
        
    def get_all(self):
        query = "SELECT * FROM students"
        return self.conn.execute(query).fetchall()
    
    def get_by_id(self, id):
        query = "SELECT * FROM students WHERE id = ?"
        return self.conn.execute(query, (id,)).fetchone()
    
    def get_by_major(self, major):
        query = "SELECT * FROM students WHERE major = ?"
        return self.conn.execute(query, (major,)).fetchall()
    
    def update(self, record_id, name, birth_date, major):
        query = "UPDATE students SET name = ?, birth_date = ?, major = ? WHERE id = ?"
        self.conn.execute(query, (name, birth_date, major, record_id))
        self.conn.commit()
        
    def delete(self, record_id):
        query = "DELETE FROM students WHERE id = ?"
        self.conn.execute(query, (record_id,))
        self.conn.commit()