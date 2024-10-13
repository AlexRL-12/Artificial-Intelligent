class EntranceRepository():

  def __init__(self, connection):
    self.connection = connection
    self.cursor = self.connection.cursor()

  def create(self, user_id, file_path, allowed):
    sql = 'INSERT INTO "entrance" (user_id, file_path, allowed) VALUES (%s, %s, %s)'

    values = (user_id, file_path, allowed)

    self.cursor.execute(sql, values)
    self.connection.commit()

  def get_user_entrace_distribution(self):
    sql = 'SELECT u.id, u.name, count(e.id) FROM entrance e INNER JOIN "user" u ON u.id = e.user_id GROUP BY u.name, u.id'
    self.cursor.execute(sql)
    return self.cursor.fetchall()

  def get_daily_entrace_distribution(self):
    sql = """
    select 
      count(CASE WHEN allowed = true THEN 1 END) AS allowed_entrances, 
      count(CASE WHEN allowed = false THEN 1 END) AS no_allowed_entrances,
      DATE(date) as date 
    FROM entrance GROUP BY DATE(date)
    ORDER BY date ASC
    """

    self.cursor.execute(sql)
    return self.cursor.fetchall()
  
  def find(self):
    sql = """
      SELECT 
        e.id::text as id, 
          CASE 
            WHEN u.name IS NOT NULL 
              THEN u.name 
              ELSE 'Desconocido' 
          END as name, 
          to_char(e."date", 'HH24:MI:SS') as date, 
          CASE 
            WHEN e.allowed = true 
              THEN 'Permitido' 
              ELSE 'Denegado' 
          END as allowed
      FROM entrance e LEFT JOIN "user" u ON u.id = e.user_id 
      WHERE DATE(e.date) = CURRENT_DATE 
      ORDER BY e."date" DESC
    """

    self.cursor.execute(sql)
    return self.cursor.fetchall()
