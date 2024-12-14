from database.connection import get_db_connection

class Article:
    def __init__(self, title, content, author_id, magazine_id):
        # Validate title
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        # Validate content
        if not isinstance(content, str) or len(content) == 0:
            raise ValueError("Content must be a non-empty string.")

        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

        # Insert into database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                       (self.title, self.content, self.author_id, self.magazine_id))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f"<Article {self.title}>"
