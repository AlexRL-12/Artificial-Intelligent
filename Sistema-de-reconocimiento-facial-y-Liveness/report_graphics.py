import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def show_user_stats_graph(stats):
  name = 1; count = 2
  
  df = pd.DataFrame(stats)
  plt.bar(df[name], df[count])
  plt.xlabel('Usuario')
  plt.ylabel('Entradas')

  plt.title('Entradas por usuario')
  plt.grid(True)

  plt.show()

def show_daily_stats_graph(stats):
    allowed_entrances = 0
    no_allowed_entrances = 1
    date = 2

    df = pd.DataFrame(stats)

    x = df[date]
    x_axis = np.arange(len(x))

    y1 = df[allowed_entrances]
    y2 = df[no_allowed_entrances]

    print(df)

    plt.bar(x_axis - 0.2, y1, 0.4, label='Entradas permitidas')
    plt.bar(x_axis + 0.2, y2, 0.4, label='Entradas no permitidas')
    plt.xticks(x_axis, x)

    plt.xlabel('Fecha')
    plt.ylabel('Cantidad de entradas')
    plt.legend()
    plt.title('Intentos de entrada por día')
    plt.grid(True)

    plt.show()

