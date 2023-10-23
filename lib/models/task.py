# lib/models/toDo.py
from . import CONN, CURSOR 
from datetime import datetime
from .person import Person

class Task:

    all = {}

    def __init__(self, task, due_date, person_id,  id = None):
        self.id = id
        self.task = task
        self.due_date = due_date
        self.person_id = person_id
        

    def __repr__(self):
        return f"Person Id: {self.person_id}, Task: {self.task}, Due Date: {self.due_date}"
    
    @property
    def task(self):
        return self._task
    
    @task.setter
    def task(self, value):
        if isinstance(value, str) and len(value):
            self._task = value
        else:
            raise ValueError(
                "Task must be a string"
            )
    
    @property
    def due_date(self):
        return self._due_date
    
    @due_date.setter
    def due_date(self, value):

        try:
            format = '%m-%d-%Y'
            datetime.strptime(value, format)
            self._due_date = value
        except:
            raise ValueError("Due date must be in the following format 'mm-dd-yyyy'")
            
        
    
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task TEXT,
            due_date TEXT,
            person_id INTEGER,
            FOREIGN KEY (person_id) REFERENCES People(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS tasks
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO tasks (task, due_date, person_id)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.task, self.due_date, self.person_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, task, due_date, person_id):
        toDo = cls(task, due_date, person_id)
        toDo.save()
        return toDo

    def update(self):
        sql = """
            UPDATE tasks
            SET task = ?, due_date = ?, person_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.task, self.due_date, self.person_id, self.id))
        CONN.commit()

    def delete(self):

        sql = """
            DELETE FROM tasks
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
       
        toDo = cls.all.get(row[0])

        if toDo:
            toDo.task = row[1]
            toDo.due_date = row[2]
            toDo.person_id = row[3]
        else:
            toDo = cls(row[1], row[2], row[3])
            toDo.id = row[0]
            cls.all[toDo.id] = toDo
        return toDo

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM tasks
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        
        sql = """
            SELECT *
            FROM tasks
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_task(cls, task):
    
        sql = """
            SELECT *
            FROM tasks
            WHERE task is ?
        """

        row = CURSOR.execute(sql, (task,)).fetchone()
        return cls.instance_from_db(row) if row else None


    def person(self):
        from .person import Person

      
        sql = """
                SELECT * FROM People
                WHERE id = ?
        """
            
    
        CURSOR.execute(sql, (self.person_id,),)

        row = CURSOR.fetchone()
        return Person.instance_from_db(row) if row else None
    



