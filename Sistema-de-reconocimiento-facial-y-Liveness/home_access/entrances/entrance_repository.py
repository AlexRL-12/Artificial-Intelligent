class EntranceRepository():

  def __init__(self, connection):
    self.connection = connection
    self.cursor = self.connection.cursor()

  def create(self, user_id, file_path, allowed):
    sql = 'INSERT INTO "entrance" (user_id, file_path, allowed) VALUES (%s, %s, %s)'

    values = (user_id, file_path, allowed)

    self.cursor.execute(sql, values)
    self.connection.commit()