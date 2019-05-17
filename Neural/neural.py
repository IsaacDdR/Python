#import the libraries 
from numpy import exp, array, dot, random, tanh

#Class to create a neural 
#network with a single neuron

class NeuralNetwork():

    def _init_(self):

        #Using a random seed 
        #to ensure we get the same weights in every run

        random.seed(1)

         #3x 1 Weight matrix

        self.weight_matrix = 2 * random.random(3, 1) - 1

    #Tanh function 
    def tanh(self, x):
        return tanh(x)

    #Tanh derivate for calculating gradients
    def tanh_derivative(self, x):
        return 1.0 - tanh(x) ** 2

    def train(self, train_inputs, train_outputs, num_train_iterations):

        #number of iterations we want to perform for this set of input
        for iteration in range (num_train_iterations):
            output = self.forward_propagation(train_inputs)

            error = train_outputs - output

            adjustment = dot(train_inputs.T, error* self.tanh_derivative(output))

            self.weight_matrix += adjustment


    if __name__ == "__main__":

        neural_network = NeuralNetwork()

        print ("Random weights at the start of the training")
        print (neural_network.weight_matrix)

        train_inputs  = array([[0,0,1], [1,1,1],[1,0,1],[0,1,1]])
        train_outputs = ([[0,1,1,0]]).T 

        neural_network.train(train_inputs, train_outputs, 10000)

        print("New weights after training")
        print(neural_network.weight_matrix)

        print("Testing network on new examples")
        print(neural_network.forward_propagation(array([1,0,0])))
    

    