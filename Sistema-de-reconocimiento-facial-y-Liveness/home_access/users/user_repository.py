class UserRepository:
  def __init__(self, connection):
    self.connection = connection
    self.cursor = self.connection.cursor()

  def create(self, name, user, password, file_path):
    sql = 'INSERT INTO "user" (name, username, password, file_path, house_id) VALUES (%s, %s, %s, %s, 1)'
    values = (name, user, password, file_path)

    self.cursor.execute(sql, values)
    self.connection.commit()

  def find_user_by_username(self, username):
    if not username:
      return None

    sql = 'SELECT * FROM "user" WHERE UPPER(username) = UPPER(%s)'
    values = (username,)
    print(sql, values)
    self.cursor.execute(sql, values)
    return self.cursor.fetchone()
