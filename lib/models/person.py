# lib/models/person.py
from models.__init__ import CONN, CURSOR

class Person:

    all = {}

    def __init__(self, name, id = None):
        self.name = name
        self.id = id
    
    def __repr__(self):
        return f"Name: {self.name}"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value):
            self._name = value
        else:
           raise ValueError("name must be a valid string")


    @classmethod
    def create_table(cls):

        sql = """ CREATE TABLE IF NOT EXISTS People(
                    id INTEGER PRIMARY KEY,
                    name TEXT
                    )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """ DROP TABLE IF EXISTS People """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """ INSERT INTO People (name)
            VALUES(?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name):
        person = cls(name)
        person.save()
        return person 
    
    def update(self):

        sql = """
                UPDATE People 
                SET name = ?
                WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
                DELETE FROM People
                WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        person = cls.all.get(row[0])

        if person:
            person.name = row[1]
        else:
            person = cls(row[1])
            person.id = row[0]
            cls.all[person.id] = person    
        return person 
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * from People
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
                SELECT * 
                FROM People 
                WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
        
    @classmethod
    def find_by_name(cls, name):
        sql = """
                SELECT * 
                FROM People 
                WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def tasks(self):
        from .task import Task

        sql = """
                SELECT *
                FROM tasks
                WHERE person_id = ?
                """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        if rows:
            return [Task.instance_from_db(row) for row  in rows]
        else:
            return print("This person has no tasks to complete!")
    






    
    


    
    