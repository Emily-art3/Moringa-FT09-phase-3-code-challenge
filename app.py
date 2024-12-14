from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Database connection
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid

    # Create magazine
    cursor.execute('SELECT id FROM magazines WHERE name = ?', (magazine_name,))
    result = cursor.fetchone()
    if result:
        magazine_id = result["id"]
    else:
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
        magazine_id = cursor.lastrowid

    # Create article
    cursor.execute(
        'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
        (article_title, article_content, author_id, magazine_id)
    )

    conn.commit()

    # Fetch data for testing
    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display data
    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(name=magazine["name"], category=magazine["category"], id=magazine["id"]))

    print("\nAuthors:")
    for author in authors:
        print(Author(name=author["name"], id=author["id"]))

    print("\nArticles:")
    for article in articles:
        print(Article(title=article["title"], content=article["content"], author_id=article["author_id"], magazine_id=article["magazine_id"]))

if __name__ == "__main__":
    main()
