#NOTA: Es importante importar las librerias antes de ejecutar el programa
#Los siguientes comandos te ayudaran:
# pip install matplotlib 
# pip install numpy

import numpy as np
import matplotlib.pyplot as plt

# Función de activación binaria (función escalón)
def step_function(z):
    return np.where(z >= 0, 1, 0)

# Función de activación sigmoide
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Función de activación ReLU
def relu(z):
    return np.maximum(0, z)

# Función de activación tangente hiperbólica (tanh)
def tanh(z):
    return np.tanh(z)

# Función de activación softmax (para problemas de clasificación multiclase)
def softmax(z):
    exp_z = np.exp(z - np.max(z))
    return exp_z / exp_z.sum(axis=0, keepdims=True)

class Perceptron:
    def __init__(self, input_size, activation_function):
        self.weights = np.random.randn(input_size)
        self.bias = np.random.randn()
        self.activation_function = activation_function
        
    def train(self, X, y, learning_rate=0.1, epochs=100):
        for epoch in range(epochs):
            for i in range(len(X)):
                z = np.dot(X[i], self.weights) + self.bias
                a = self.activation_function(z)
                error = y[i] - a
                self.weights += learning_rate * error * X[i]
                self.bias += learning_rate * error
    
    def predict(self, X):
        z = np.dot(X, self.weights) + self.bias
        return self.activation_function(z)

# Diccionario de operaciones
operations = {
    1: ("OR", np.array([[0, 0], [0, 1], [1, 0], [1, 1]]), np.array([0, 1, 1, 1])),
    2: ("XOR", np.array([[0, 0], [0, 1], [1, 0], [1, 1]]), np.array([0, 1, 1, 0])),
    3: ("AND", np.array([[0, 0], [0, 1], [1, 0], [1, 1]]), np.array([0, 0, 0, 1]))
}

# Funciones de activación disponibles
activation_functions = {
    1: step_function,
    2: sigmoid,
    3: relu,
    4: tanh,
    5: softmax
}

while True:
    try:
        print("Seleccione una operación:")
        for key, (operation_name, _, _) in operations.items():
            print(f"{key}: {operation_name}")

        choice = int(input("Ingrese el número correspondiente a la operación deseada: "))
        if choice in operations:
            break
        else:
            print("Operación no válida. Por favor, elija un número válido.")
    except ValueError:
        print("Entrada no válida. Ingrese un número válido.")

# Obtener los datos de la operación seleccionada
selected_operation, X, y = operations[choice]

while True:
    try:
        print("Seleccione una función de activación:")
        for key, activation_name in activation_functions.items():
            print(f"{key}: {activation_name.__name__}")

        activation_choice = int(input("Ingrese el número correspondiente a la función de activación deseada: "))
        if activation_choice in activation_functions:
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")
    except ValueError:
        print("Entrada no válida. Ingrese un número válido.")

selected_activation_function = activation_functions[activation_choice]

print(f"Para la operación {selected_operation}, ingrese dos valores (0 o 1) para las entradas.")

input_data = []
for i in range(2):
    while True:
        try:
            val = int(input(f"Ingrese el valor {i + 1}: "))
            if val not in [0, 1]:
                print("Por favor, ingrese un valor válido (0 o 1).")
            else:
                input_data.append(val)
                break
        except ValueError:
            print("Entrada no válida. Ingrese un valor válido (0 o 1).")

# Crear y entrenar el perceptrón con la función de activación seleccionada
perceptron = Perceptron(input_size=2, activation_function=selected_activation_function)
perceptron.train(X, y)

# Realizar predicciones
user_input = np.array(input_data)
prediction = perceptron.predict(user_input)

if activation_choice == 5:
    meaning = "La predicción se muestra como una distribución de probabilidad."
else:
    meaning = "La predicción indica VERDADERO si la salida es mayor que 0.5; FALSO en caso contrario."

print(meaning)

# Gráfica para visualizar las predicciones (solo para funciones de activación no softmax)
if activation_choice != 5:
    x = np.arange(0, 1.1, 0.1)
    y = np.arange(0, 1.1, 0.1)
    xx, yy = np.meshgrid(x, y)
    input_grid = np.c_[xx.ravel(), yy.ravel()]
    predictions = perceptron.predict(input_grid)
    predictions = predictions.reshape(xx.shape)

    plt.contourf(xx, yy, predictions, cmap=plt.cm.Paired, alpha=0.8)
    plt.scatter(user_input[0], user_input[1], c='red', marker='x', s=100)
    plt.xlabel('Entrada 1')
    plt.ylabel('Entrada 2')
    plt.title(f'Predicción del Perceptrón para {selected_operation} usando {selected_activation_function.__name__}')
    plt.show()
