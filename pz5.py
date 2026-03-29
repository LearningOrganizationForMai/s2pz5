import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

class PostgreSQL:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST'),
            port=int(os.getenv('POSTGRES_PORT')),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            database=os.getenv('POSTGRES_DATABASE')
        )
        self.cursor = self.conn.cursor()
        print('PostgreSQL подключен')

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()


pg = PostgreSQL()
print('Данные из employees:')
try:
    data = pg.query('SELECT * FROM employees LIMIT 5')
    for row in data:
        print(f'  {row}')
except Exception as e:
    print(f'Ошибка: {e}')

print('Данные из positions:')
try:
    data = pg.query('SELECT * FROM positions LIMIT 5')
    for row in data:
        print(f'{row}')
except Exception as e:
    print(f'Ошибка: {e}')

print('Данные из suppliers:')
try:
    data = pg.query('SELECT * FROM suppliers LIMIT 5')
    for row in data:
        print(f'{row}')
except Exception as e:
    print(f'Ошибка: {e}')

pg.close()
