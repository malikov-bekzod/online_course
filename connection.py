from os import getenv
import psycopg2 as psql
from dotenv import load_dotenv

load_dotenv()

connection_db = psql.connect(
    host = getenv("DATABASE_HOST"),
    database = getenv("DATABASE_NAME"),
    user = getenv("DATABASE_USER"),
    password = getenv("DATABASE_PASSWORD")
)

# cursor = connection_db.cursor()
# cursor.execute("SELECT current_database()")

# result = cursor.fetchone()
# print(result)