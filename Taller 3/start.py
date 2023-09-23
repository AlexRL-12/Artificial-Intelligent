#Machine Learning supervisado-Regresión logística

# Importar bibliotecas
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Leer los datos
data = pd.read_csv('/imdb_top_1000.csv')
data

# Seleccionar las colummnas requeridas
colInteres = ['Series_Title','Released_Year','Certificate','Runtime','Genre','IMDB_Rating','Overview','Meta_score','Director']
datainteres = data[colInteres]
datainteres = datainteres.dropna()

# Separar los datos en conjuntos de entrenamiento y prueba
X=datainteres [['IMDB_Rating']]
Y= datainteres [['Meta_score']]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Entrenar el modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, Y_train)

# Predecir los resultados para el conjunto de datos de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = model.score(X_test, Y_test)
print("Precisión:", accuracy)

# Crear un gráfico de barras
plt.bar(datainteres["Certificate"].unique(), datainteres["Certificate"].value_counts())

# Agregar un título al gráfico
plt.title("Frecuencia de cada certificado")

# Agregar etiquetas a los ejes
plt.xlabel("Certificado")
plt.ylabel("Frecuencia")

# Mostrar el gráfico
plt.show()

