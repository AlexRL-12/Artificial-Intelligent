from database import DatabaseConnection
from home_access.entrances.entrance_repository import EntranceRepository
from admin_reports.graphics import ReportGraphics
import matplotlib.pyplot as plt

connection = DatabaseConnection().connect()
entranceRepository = EntranceRepository(connection)

class Reports:
  def __init__(self):
    self.graphics = ReportGraphics(plt)

  def show_user_stats(self):
    user_distribution = entranceRepository.get_user_entrace_distribution()
    self.graphics.show_user_stats_graph(user_distribution)

  def show_daily_distribution(self):
    daily_distribution = entranceRepository.get_daily_entrace_distribution()
    self.graphics.show_daily_stats_graph(daily_distribution)

  def show_daily_entraces(self):
    daily_entraces = entranceRepository.find()
    self.graphics.show_today_entraces(daily_entraces)

  def show_reports(self, screen_resolution):
    self.show_user_stats()
    self.show_daily_distribution()
    self.show_daily_entraces()
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    figManager = plt.get_current_fig_manager()
    figManager.resize(screen_resolution[0], screen_resolution[1])
    plt.show()
