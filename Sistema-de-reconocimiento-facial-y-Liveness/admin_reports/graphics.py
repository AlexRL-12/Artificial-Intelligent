import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

class ReportGraphics:
  def __init__(self, plt: plt):
    self.plt = plt
    self.colums = 2
    self.rows = 2
    self.gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[1, 1])

  def show_user_stats_graph(self, stats):
    name = 1; count = 2
    
    df = pd.DataFrame(stats)
    plt.subplot(self.gs[0, 0])
    plt.bar(df[name], df[count])
    plt.xlabel('Usuario')
    plt.ylabel('Entradas')

    plt.title('Entradas por usuario')
    plt.grid(True)

  def show_daily_stats_graph(self, stats):
      allowed_entrances = 0
      no_allowed_entrances = 1
      date = 2

      df = pd.DataFrame(stats)

      x = df[date]
      x_axis = np.arange(len(x))

      y1 = df[allowed_entrances]
      y2 = df[no_allowed_entrances]

      plt.subplot(self.gs[0, 1])
      plt.bar(x_axis - 0.2, y1, 0.4, label='Entradas permitidas')
      plt.bar(x_axis + 0.2, y2, 0.4, label='Entradas no permitidas')
      plt.xticks(x_axis, x)

      plt.xlabel('Fecha')
      plt.ylabel('Cantidad de entradas')
      plt.legend()
      plt.title('Intentos de entrada por día')
      plt.grid(True)

  def show_today_entraces(self, stats):
    data = stats
    if(len(stats) == 0):
      data = [('Sin datos', 'Sin datos', 'Sin datos', 'Sin datos')]

    labels = ('ID', 'Usuario', 'Hora', 'Acceso')
    df = pd.DataFrame(data)
    plt.subplot(self.gs[1, :])
    self.plt.axis('off')
    self.plt.title('Entradas hoy')
    self.plt.table(colLabels=labels, cellText=df.values, loc='center')