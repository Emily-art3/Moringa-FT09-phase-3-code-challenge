class Author:
    def __init__(self, name):
        # Validate name
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")

        self.name = name

        # Insert into database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO authors (name) VALUES (?)",
            (name,),
        )
        conn.commit()
        self.id = cursor.lastrowid  # Store the generated id
        conn.close()

    def __repr__(self):
        return f"<Author {self.name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot change the name of an author.")


    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM articles WHERE author_id = ?", (self.id,)
        )
        articles = cursor.fetchall()
        conn.close()
        return [dict(article) for article in articles]
