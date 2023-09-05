import numpy as np

class AdvancedPerceptron:

    def __init__(self, n_inputs, learning_rate=0.1):
        
        self.weights = np.random.randn(n_inputs)
        self.learning_rate = learning_rate

    def sigmoid(self, x):
        
        return 1 / (1 + np.exp(-x))

    def predict(self, x):
        
        weighted_sum = np.dot(x, self.weights)
        prediction = self.sigmoid(weighted_sum)
        return prediction

    def train(self, X, y, epochs=100):
        for epoch in range(epochs):
            for i, x in enumerate(X):
                # Realizamos la predicción
                prediction = self.predict(x)
                
                error = y[i] - prediction
                # Actualizamos los pesos usando la tasa de aprendizaje
                self.weights += self.learning_rate * error * x

    def evaluate(self, X, y):
        correct = 0
        for i, x in enumerate(X):
            
            prediction = self.predict(x)
            # Clasificamos como 1 si la predicción es mayor o igual a 0.5, de lo contrario, como 0
            y_pred = 1 if prediction >= 0.5 else 0
            if y_pred == y[i]:
                correct += 1
            print(f"x = {x}, y = {y[i]}, y_pred = {y_pred}")
        
        accuracy = correct / len(X)
        print(f"Accuracy: {accuracy * 100:.2f}%")

def main():
    # Datos de entrenamiento
    X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
    y = np.array([1, 0, 0, 1])

    p = AdvancedPerceptron(2, learning_rate=0.1)
    p.train(X, y, epochs=1000)
    p.evaluate(X, y)

if __name__ == "__main__":
    main()
