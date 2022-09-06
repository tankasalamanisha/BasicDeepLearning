from subprocess import getoutput
from numpy import exp, array, random, dot 

class SigmoidNeuralNet():
    """Class to implement sigmoid single neural network.
    """
    
    def __init__(self) -> None:
        """Sets the random seed and defines the random synaptic weights
        """
        random.seed(1)
        
        self.synaptic_weights = 2* random.random((3,1)) -1
    
    def sigmoid(x:float):
        """Function to generate a sigmoid value for a value.

        Args:
            x (float): Value to get the sigmoid transform.
        """
        return 1 / (1+exp(-x))
    
    def getoutput(self, train_inputs:array):
        """Function to return values after applying the sigmoid function.

        Args:
            train_inputs (array): training data points in the format of array
        """
        return self.sigmoid(dot(train_inputs, self.synaptic_weights))
    
    def sig_grad(x:float):
        """_summary_

        Args:
            x (float): Value for getting sigmoid gradient

        Returns:
            _float_: sigmoid gradient
        """
        return x * (1 - x)
    
    def train(self, train_inputs: array, train_outputs:array, iterations: int):
        for iteration in range(iterations):
            
            output = getoutput(train_inputs)
            
            error = train_outputs - output
            
            adjustment = dot(train_inputs.T, error*self.sig_grad(output))
            
            self.synaptic_weights = self.synaptic_weights + adjustment

if __name__ == "__main__":
    train_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    train_outputs = array([[0, 1, 0, 1]]).T
    
    sigmoid_nn = SigmoidNeuralNet()
    
    print("weights before training")
    print(sigmoid_nn.synaptic_weights)
    
    sigmoid_nn.train(train_inputs, train_outputs, 10000)
    
    print("weights after training")
    print(sigmoid_nn.synaptic_weights)