import math
import random

class FeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases randomly
        self.W1 = self.random_matrix(self.input_size, self.hidden_size)
        self.b1 = [random.random() for _ in range(self.hidden_size)]
        self.W2 = self.random_matrix(self.hidden_size, self.output_size)
        self.b2 = [random.random() for _ in range(self.output_size)]

    def random_matrix(self, rows, cols):
        return [[random.random() for _ in range(cols)] for _ in range(rows)]

    def sigmoid(self, z):
        return 1 / (1 + math.exp(-z))

    def sigmoid_derivative(self, z):
        return z * (1 - z)

    def forward(self, X):
        self.Z1 = [sum(x * w for x, w in zip(X, row)) + b for row, b in zip(self.W1, self.b1)]
        self.A1 = [self.sigmoid(z) for z in self.Z1]
        self.Z2 = [sum(a * w for a, w in zip(self.A1, row)) + b for row, b in zip(self.W2, self.b2)]
        self.A2 = [self.sigmoid(z) for z in self.Z2]
        return self.A2

    def backward(self, X, y, learning_rate=0.01):
        m = len(X)

        # Calculate the error for output layer
        dZ2 = [a2 - yi for a2, yi in zip(self.A2, y)]  # This should already be a list
        dW2 = [[sum(a1 * dz2 for a1, dz2 in zip(self.A1, dZ2)) / m] for _ in range(self.output_size)]
        db2 = [sum(dz2) / m for dz2 in dZ2]

        # Calculate the error for hidden layer
        dA1 = [sum(w2 * dz2 for w2, dz2 in zip(self.W2, dZ2)) for _ in range(self.hidden_size)]
        dZ1 = [da1 * self.sigmoid_derivative(a1) for da1, a1 in zip(dA1, self.A1)]
        dW1 = [[sum(x * dz1 for x, dz1 in zip(X, dZ1)) / m] for _ in range(self.hidden_size)]
        db1 = [sum(dz1) / m for dz1 in dZ1]

        # Update weights and biases
        self.W1 = [[w - learning_rate * dw for w, dw in zip(row, dw_row)] for row, dw_row in zip(self.W1, dW1)]
        self.b1 = [b - learning_rate * db for b, db in zip(self.b1, db1)]
        self.W2 = [[w - learning_rate * dw for w, dw in zip(row, dw_row)] for row, dw_row in zip(self.W2, dW2)]
        self.b2 = [b - learning_rate * db for b, db in zip(self.b2, db2)]

    def train(self, X, y, epochs=10000, learning_rate=0.01):
        for _ in range(epochs):
            for i in range(len(X)):
                self.forward(X[i])
                self.backward(X[i], y[i], learning_rate)

    def predict(self, X):
        output = self.forward(X)
        return [1 if o > 0.5 else 0 for o in output]

# Example usage
if __name__ == "__main__":
    # Input data (XOR problem)
    X = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    # Output data (XOR result)
    y = [
        [0],
        [1],
        [1],
        [0]
    ]

    # Create and train the neural network
    nn = FeedForwardNN(input_size=2, hidden_size=4, output_size=1)
    nn.train(X, y, epochs=10000, learning_rate=0.1)

    # Make predictions
    predictions = [nn.predict(x) for x in X]
    print("Predictions after training:")
    print(predictions)
