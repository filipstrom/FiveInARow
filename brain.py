import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def forward(self, inputs):
        return sigmoid(np.dot(inputs, self.weights) + self.bias)

class Layer:
    neurons = None

    def __init__(self, number_of_inputs, number_of_neurons):
        self.neurons = [Neuron(np.random.randn(number_of_inputs), np.random.randn()) for _ in range(number_of_neurons)]

    def forward(self, inputs):
        return np.array([neuron.forward(inputs) for neuron in self.neurons])

class NeuralNetwork:
    layers = None

    def __init__(self, number_of_inputs, neurons_per_layer, number_of_moves):
        print(number_of_inputs, neurons_per_layer[0], neurons_per_layer[1], number_of_moves)
        self.layers = [
            Layer(number_of_inputs, neurons_per_layer[0]),
            Layer(neurons_per_layer[0], neurons_per_layer[1]),
            Layer(neurons_per_layer[1], number_of_moves)
        ]

    def predict(self, inputs):
        current_outputs = inputs
        for layer in self.layers:
            current_outputs = layer.forward(current_outputs)
        return current_outputs

    def train(self, training_data, labels):
        # Här skulle du implementera träning, t.ex. med backpropagation
        pass
