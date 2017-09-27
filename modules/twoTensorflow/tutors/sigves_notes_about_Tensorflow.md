# TensorFlow
Alot of the description is copied from Tensorflow it self (https://www.tensorflow.org/get\_started/get\_started).

## Tensors
The central unit of data in TensorFlow is the tensor. A tensor consists of a set of primitive values shaped into an array of any number of dimensions. A tensor's rank is its number of dimensions. Here are some examples of tensors:

- `3 # a rank 0 tensor; this is a scalar with shape []`
- `[1., 2., 3.] # a rank 1 tensor; this is a vector with shape [3]`
- `[[1., 2., 3.], [4., 5., 6.]] # a rank 2 tensor; a matrix with shape [2, 3]`
- `[[[1., 2., 3.]], [[7., 8., 9.]]] # a rank 3 tensor with shape [2, 1, 3]`

> Sigves tip: Count how many opening brackets. This gives the rank.

_Important_:
Node takes zero or more tensors as inputs and produces a tensor as an output


## Computational Graph
A computational graph is a series of TensorFlow operations arranged into a graph of nodes.


## TensorBoard
- Display a picture of he computational Graph


## TensorFlow Constants
- TensorFlow constants, it takes no inputs, and it outputs a value it stores internally. 
- To actually evaluate the nodes, we must run the computational graph within a session. A session encapsulates the control and state of the TensorFlow runtime.

IMPORTANT : Constants gets initialized when you call `tf.constants`

## TensorFlow Operations
A Operator in TensorFlow is also a tensor node.

- Thus `tf.add(node1,node2)` = node1 + node 2 (+ gets translated to tf.add())

## TensorFlow placeholder : promise to provide a value later.
Using placeholders can make a function alot more general and modular. 
- tf.placeholder(tf.dataType)
 - i.e
  - `a = tf.placeholder(tf.float32)`

## TensorFlow Making the Model Trainable
To make a model trainable, we need to be able to modify the graph to get new outputs with the same input.
Variables allow us to add trainable parameters to a graph.

## TensorFlow Variables
Variables allow us to add trainable parameters to a graph. They are constructed with a type and initial value:
`w = tf.Variable([.3), dtype=tf.float32)`

IMPORTANT : Variables does not get initialized when calling `tf.Variable()`, To initialize all the variables in a TensorFLow program, you must explicitly call a special operations
`
init = tf.global_variables_initializer()
sess.run(init)
`

To know if the model we have created is good or to know how good it is, we need to evaluate the model on training data. Thus we need a `y` placeholder to provide the desired values, and we need to write a `loss` function (loss = evaluation)

### LOSS FUNCTION
A loss function measures how far apart the current model is from the provided data


The whole point of machine learning is to find the correct model parameters automatically. 

## TensorFlow Optimizers
TensorFlow provides optimizers that slowly change each variable in order to minimize the loss function. The simplest optimizer is gradient descent.

### Gradient Descent : Gradvis nedtrapping
Gradient descent. It modifies each variable according to the magnitude of the derivative of loss with respect to that variable.

#### Derivitives
TensorFlow can automatically produce derivatives given only a description of the model using the function tf.gradients

## TensorFlow Estimator
`tf.estimator` is a high-level TensorFlow library that simplifies the mechanics of machine learning, including the following:

- running training loops
- running evaluation loops
- managing data sets
- tf.estimator defines many common models.


