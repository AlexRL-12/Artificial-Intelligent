import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

class DatabaseConnection:
  def __init__(self):
    self.host = os.environ.get('DB_HOST')
    self.user = os.environ.get('DB_USER')
    self.password = os.environ.get('DB_PASSWORD')
    self.database = os.environ.get('DB_NAME')
    self.port = os.environ.get('DB_PORT')

  def connect(self):
    print(self.host, self.user, self.password, self.database, self.port)
    connection = psycopg2.connect(
      host=self.host, 
      user=self.user, 
      password=self.password, 
      dbname=self.database, 
      port=self.port
    )

    return connection
