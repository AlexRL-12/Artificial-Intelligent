import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import warnings
import time

warnings.filterwarnings("ignore")

# Leer los datos
data = pd.read_csv('Datos-emisiones.csv')

# Seleccionar las columnas requeridas
colInteres = ['Fugitive emissions', 'Industrial processes','Energy','Energy indust','Manufacturing','Transport','Other sectors','Agriculture' ,'Waste', 'num']
datainteres = data[colInteres]
datainteres = datainteres.dropna()

# Separar los datos en conjuntos de entrenamiento y prueba
X = datainteres[['Energy']]
Y = datainteres[['Energy indust']]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Función para realizar regresión lineal
def regression_linear():
    model = LinearRegression()
    model.fit(X_train, Y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(Y_test, y_pred)
    print("Coeficiente R^2 de Regresión Lineal:", r2)

    # Mostrar los parámetros del modelo
    print("Parámetros del modelo de regresión lineal:")
    print("Coeficientes:", model.coef_)
    print("Ordenada al origen:", model.intercept_)

    plt.scatter(X_test, Y_test, label='Datos reales')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regresión Lineal')
    plt.xlabel("Energy")
    plt.ylabel("Energy indust")
    plt.title("Regresión Lineal")
    plt.legend()
    plt.show()

# Función para realizar Árboles de Decisión
def decision_tree():
    model = DecisionTreeRegressor(max_depth=5, random_state=42)
    model.fit(X_train, Y_train)

    X_test_sorted = X_test.sort_values(by='Energy')

    y_pred = model.predict(X_test_sorted)

    r2 = r2_score(Y_test, model.predict(X_test))
    print("Coeficiente R^2 de Árboles de Decisión:", r2)

    # Mostrar la profundidad máxima del árbol
    print("Profundidad máxima del árbol:", model.tree_.max_depth)

    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, Y_test, label='Datos reales')
    plt.plot(X_test_sorted, y_pred, color='green', linewidth=2, label='Árboles de Decisión')
    plt.xlabel("Energy")
    plt.ylabel("Energy indust")
    plt.title("Árboles de Decisión")
    plt.legend()
    plt.show()

# Función para realizar K-Means
def k_means():
    kmeans = KMeans(n_clusters=5, random_state=42)
    datainteres['Cluster'] = kmeans.fit_predict(X)

    silhouette_avg = silhouette_score(X, kmeans.labels_)
    print("Puntuación de silueta de K-Means:", silhouette_avg)

    # Mostrar nombres de los clusters
    cluster_names = datainteres['Cluster'].unique()
    for name in cluster_names:
        print(f"Cluster {name}: {datainteres[datainteres['Cluster'] == name].index.tolist()}")

    # Obtener los centroides de los clusters
    centroids = kmeans.cluster_centers_

    # Crear la gráfica de dispersión con etiquetas y centroides
    plt.figure(figsize=(10, 6))
    plt.scatter(X, Y, c=datainteres['Cluster'], cmap='viridis')
    plt.scatter(centroids, [0] * len(centroids), c='red', marker='X', s=100, label='Centroides')
    plt.xlabel("Energy")
    plt.ylabel("Energy indust")
    plt.title("Resultados de K-Means")
    plt.legend()

    # Etiquetar los puntos de datos con el número de cluster
    for i, txt in enumerate(datainteres['Cluster']):
        plt.annotate(txt, (X.iloc[i], 0), fontsize=8)  # Usamos 0 como coordenada Y para un espacio unidimensional

    plt.show()

# Menú principal
while True:
    print("Seleccione un modelo:")
    print("1. Regresión Lineal")
    print("2. Árboles de Decisión")
    print("3. K-Means")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción que desea: ")

    if opcion == '1':
        start_time = time.time()
        regression_linear()
        end_time = time.time()
        print("Tiempo de ejecución:", end_time - start_time, "segundos")
    elif opcion == '2':
        start_time = time.time()
        decision_tree()
        end_time = time.time()
        print("Tiempo de ejecución:", end_time - start_time, "segundos")
    elif opcion == '3':
        start_time = time.time()
        k_means()
        end_time = time.time()
        print("Tiempo de ejecución:", end_time - start_time, "segundos")
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
