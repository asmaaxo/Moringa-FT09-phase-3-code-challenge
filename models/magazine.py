from database.connection import get_db_connection
from models.author import Author

class Magazine:
    def __init__(self, id, name, category="General"):
        # Delete any existing magazine with the same id
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("DELETE FROM magazines WHERE id=?", (id,))

        if not isinstance(id, int):
            raise TypeError("Magazine id must be an int.")
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Magazine name must be a non-empty string.")
        if not isinstance(category, str) or len(category.strip()) == 0:
            raise ValueError("Magazine category must be a non-empty string.")

        c.execute("INSERT INTO magazines (id, name, category) VALUES (?,?,?)", (id, name, category))
        conn.commit()

        self._id = id
        self._name = name
        self._category = category

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("Magazine id must be an int.")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("UPDATE magazines SET id=? WHERE id=?", (value, self._id))
        conn.commit()
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Magazine name must be a non-empty string.")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("UPDATE magazines SET name=? WHERE id=?", (value, self._id))
        conn.commit()
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("UPDATE magazines SET category=? WHERE id=?", (value, self._id))
        conn.commit()
        self._category = value

    def __repr__(self):
        return f"<Magazine {self.name}>"
