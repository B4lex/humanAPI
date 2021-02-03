import psycopg2 as psql
from flask import g, current_app

DB_NAME = 'human_api_db'
USER = 'flask_app'
PASSWORD = 'psql'


def get_db():
    if 'db' not in g:
        g.db = psql.connect(dbname=DB_NAME, user=USER, password=PASSWORD)

    return g.db


def close_db():
    database = g.pop('db', None)
    if database:
        database.close()


def add_human(human_dict):
    db = get_db()
    with db.cursor() as cursor:
        query = ('INSERT INTO human ('
                 ''
                 ''
                 ''
                 ''
                 '')


def _init_db():
    with current_app.open_resource('init_db_schema.sql', 'r') as sql_schema:
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute(sql_schema.read())
        db.commit()



