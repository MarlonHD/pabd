import psycopg2
from decouple import config

conn = psycopg2.connect(
            host=config('DATABASE_HOST'),
            database=config('DATABASE_NAME'),
            user=config('DATABASE_USER'),
            password=config('DATABASE_PASS')
        )

conn.close()