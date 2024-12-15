from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine
class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        # Delete any existing article with same id
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("DELETE FROM articles WHERE id=?", (id,))

        if not isinstance(id, int):
            raise TypeError("Article id must be an int.")
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("Article title must be a non-empty string.")
        if not isinstance(author_id, int):
            raise TypeError("author_id must be an int.")
        if not isinstance(magazine_id, int):
            raise TypeError("magazine_id must be an int.")

        c.execute("INSERT INTO articles (id, title, content, author_id, magazine_id) VALUES (?,?,?,?,?)",
                  (id, title, content, author_id, magazine_id))
        conn.commit()

        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("Article id must be an int.")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("UPDATE articles SET id=? WHERE id=?", (value, self._id))
        conn.commit()
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Article title must be a non-empty string.")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("UPDATE articles SET title=? WHERE id=?", (value, self._id))
        conn.commit()
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("UPDATE articles SET content=? WHERE id=?", (value, self._id))
        conn.commit()
        self._content = value

    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, value):
        if not isinstance(value, int):
            raise TypeError("author_id must be an int.")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("UPDATE articles SET author_id=? WHERE id=?", (value, self._id))
        conn.commit()
        self._author_id = value

    @property
    def magazine_id(self):
        return self._magazine_id

    @magazine_id.setter
    def magazine_id(self, value):
        if not isinstance(value, int):
            raise TypeError("magazine_id must be an int.")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("UPDATE articles SET magazine_id=? WHERE id=?", (value, self._id))
        conn.commit()
        self._magazine_id = value

    def __repr__(self):
        return f"<Article {self.title}>"
