import numpy as np
import deep_learning_exam.sigmoid_function as sigm
import deep_learning_exam.identity_function as iden

class three_floor_nnetwork:

    def init_network(self):
        network = {}
        network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
        network['b1'] = np.array([0.1, 0.2, 0.3])
        network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
        network['b2'] = np.array([0.1, 0.2])
        network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
        network['b3'] = np.array([0.1, 0.2])

        return network

    def forward(self, network, x):
        W1, W2, W3 = network['W1'], network['W2'], network['W3']
        b1, b2, b3 = network['b1'], network['b2'], network['b3']
        sig = sigm.sigmoid()
        ide = iden.identity()

        a1 = np.dot(x, W1) + b1
        z1 = sig.sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        z2 = sig.sigmoid(a2)
        a3 = np.dot(z2, W3) + b3
        y = ide.identity_function(a3)

        return y

tfnn = three_floor_nnetwork()
network = tfnn.init_network()
print(network)
x = np.array([1.0, 0.5])
y =tfnn.forward(network, x)
print(y) # [0.31682703   0.69627909]