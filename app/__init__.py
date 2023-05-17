"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7lku4dadc9vlud10g-a.oregon-postgres.render.com",
        database="todo_iu7w",
        user="todo_iu7w_user",
        password="GnOtAdY9i4N8OD5baaYqr7RJHn5iKzvK")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
