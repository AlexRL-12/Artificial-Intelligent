import tensorflow as tf
from tensorflow import keras

def create_model(activation_functions):
    modelo = keras.Sequential([
        keras.layers.Input(shape=(2,)),
        keras.layers.Dense(8, activation=activation_functions[0]),
        keras.layers.Dense(8, activation=activation_functions[1]),
        keras.layers.Dense(8, activation=activation_functions[2]),
        keras.layers.Dense(8, activation=activation_functions[3]),
        keras.layers.Dense(1, activation=activation_functions[4]),
    ])
    return modelo

def train_and_evaluate(model, data, labels):
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(data, labels, epochs=1000, verbose=0)
    loss, accuracy = model.evaluate(data, labels)
    print(f"Pérdida: {loss}, Precisión: {accuracy}")
    predictions = model.predict(data)
    print(f"Predicciones:\n{predictions}\n")

def main():
    datos_entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
    etiquetas = None

    while etiquetas not in (1, 2, 3):
        print("Seleccione la etiqueta que desea usar:")
        print("1. AND")
        print("2. OR")
        print("3. XOR")
        try:
            etiquetas = int(input("Ingrese el número correspondiente a la operación: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if etiquetas == 1:
        etiquetas = [0, 1, 1, 0]  # Resultados de la operación AND
    elif etiquetas == 2:
        etiquetas = [0, 1, 1, 1]  # Resultados de la operación OR
    else:
        etiquetas = [0, 0, 0, 1]  # Resultados de la operación XOR

    activations = ['relu', 'sigmoid', 'tanh', 'softmax']

    for i in range(3):
        model = create_model([activations[i % 4], activations[(i + 1) % 4], activations[(i + 2) % 4], activations[(i + 3) % 4], activations[(i + 4) % 4]])
        print(f"Red neuronal {i + 1}:")
        train_and_evaluate(model, datos_entrada, etiquetas)

if __name__ == "__main__":
    main()
