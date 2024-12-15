from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        # Delete existing record with same id to avoid UNIQUE constraint issues
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("DELETE FROM authors WHERE id=?", (id,))
        
        if not isinstance(id, int):
            raise TypeError("Author id must be an int.")
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Author name must be a non-empty string.")

        c.execute("INSERT INTO authors (id, name) VALUES (?, ?)", (id, name))
        conn.commit()

        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("Author id must be an int.")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("UPDATE authors SET id=? WHERE id=?", (value, self._id))
        conn.commit()
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Author name must be a non-empty string.")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("UPDATE authors SET name=? WHERE id=?", (value, self._id))
        conn.commit()
        self._name = value

    def __repr__(self):
        return f"<Author {self.name}>"
