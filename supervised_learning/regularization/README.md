# Regularization

## Tasks
| File name                                                                    | Description                                                                                                                                                                          |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [0. L2 Regularization Cost](./0-l2_reg_cost.py)                              | Function `def l2_reg_cost(cost):` that calculates the cost of a neural network with L2 regularization.                                                                               |
| [1. Gradient Descent with L2 Regularization](./1-l2_reg_gradient_descent.py) | Function `def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):` that updates the weights and biases of a neural network using gradient descent with L2 regularization. |
| [2. L2 Regularization Cost](./2-l2_reg_cost.py)                              | Function `def l2_reg_cost(cost):` that calculates the cost of a neural network with L2 regularization.                                                                               |
| [3. Create a Layer with L2 Regularization](./3-l2_reg_create_layer.py)       | Function `def l2_reg_create_layer(prev, n, activation, lambtha):` that creates a tensorflow layer that includes L2 regularization.                                                   |
| [4. Forward Propagation with Dropout](./4-dropout_forward_prop.py)           | Function `def dropout_forward_prop(X, weights, L, keep_prob):` that conducts forward propagation using Dropout.                                                                      |
| [5. Gradient Descent with Dropout](./5-dropout_gradient_descent.py)          | Function `def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):` that updates the weights of a neural network with Dropout regularization using gradient descent.    |
| [6. Create a Layer with Dropout](./6-dropout_create_layer.py)                | Function `def dropout_create_layer(prev, n, activation, keep_prob):` that creates a layer of a neural network using dropout.                                                         |
| [7. Early Stopping](./7-early_stopping.py)                                   | Function `def early_stopping(cost, opt_cost, threshold, patience, count):` that determines if you should stop gradient descent early.                                                |