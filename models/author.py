class Author:
    def __init__(self, name, id=None):
        # Validate the name
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        
        # Debugging line - Indented properly inside the __init__ method
        print(f"Initializing Author with name: {name}, id: {id}")

        # Directly assign to the private attribute to bypass the setter
        self._name = name
        self.id = id

        # Insert into database if id is None
        if self.id is None:
            conn = get_db_connection()  # Ensure this function exists and returns a connection
            cursor = conn.cursor()
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
            conn.commit()
            self.id = cursor.lastrowid  # Set the id to the new row's id from the database
            conn.close()

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name (disallow changes after initialization)
    @name.setter
    def name(self, value):
        raise AttributeError("Cannot change the name of an author.")

    def __repr__(self):
        return f"<Author {self.name}>"

    def articles(self):
        # Get articles by author
        conn = get_db_connection()  # Again, ensure this is defined somewhere
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM articles WHERE author_id = ?", (self.id,)
        )
        articles = cursor.fetchall()
        conn.close()
        return [dict(article) for article in articles]  # Ensure 'article' is a dictionary-like object
