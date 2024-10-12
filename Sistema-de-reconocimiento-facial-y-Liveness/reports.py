from database import DatabaseConnection
from home_access.entrances.entrance_repository import EntranceRepository
import report_graphics as graphics

connection = DatabaseConnection().connect()
entranceRepository = EntranceRepository(connection)

def show_user_stats():
  user_distribution = entranceRepository.get_user_entrace_distribution()
  graphics.show_user_stats_graph(user_distribution)

def show_daily_distribution():
  daily_distribution = entranceRepository.get_daily_entrace_distribution()
  graphics.show_daily_stats_graph(daily_distribution)

if __name__ == '__main__':
  show_user_stats()
  show_daily_distribution()
