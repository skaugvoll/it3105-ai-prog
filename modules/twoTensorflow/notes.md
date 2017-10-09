# Notes from handed out articles.

## Implementing an Interface to TensorFlow
### The Network Scenario
A network scenario consists of:
1. A dataset serving as the basis for a classification task.
2. A specification of the network’s architecture (a.k.a. configuration): the layers of neurons, their sizes and activation functions, the cost function, etc.
3. A scheme for training and testing the network on the dataset.
4. A specification of the network behaviors to be visualized.

##### The Dataset
Has a list of features and list of class/labels (labels = output).
- Created either from data files or,
- Created from special functions


##### The Network Architecture
A dataset defines a classification task, which will give hints as to the proper neural network configurations.

Trian and error is a big part of this task, for finding the right architeture.

Important degrees of freedom are;
1. The number of hidden layers.
2. The number of nodes in each hidden layer. Different layers will typically have different sizes. 3. The activation functions used in the hidden layers and output layer.
4. The learning rate.
5. The error function (a.k.a. loss function) for backpropagation.
6. The initial range of values for network weights.

These and other factors are what determines the structure and general behavior of the network. Choosing them often constitues the hardest part of problem solving with deep learning.



