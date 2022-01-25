import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt



np.random.seed(0)
x, y = make_regression(n_samples=100, n_features=1, noise=10)
y = y.reshape(y.shape[0], 1)
# print(x)
# print(type(x))
# print(y.shape)

# matrice X ( où F = X . theta)
X = np.hstack((x, np.ones(x.shape)))
# print(X.shape)
# print(x)

# Vecteur parametres (theta0 theta1) initialisation
np.random.seed(0) # pour produire toujours le meme vecteur theta aléatoire
theta = np.random.randn(2,1)
# print(theta.shape)
# print(theta)

# 1. model F
def model(X, theta):
    return X.dot(theta)

# print(model(X, theta))

# 2. Fonction cout
def cost_function(X, y, theta):
    m = len(y)
    return 1/(2*m) * np.sum((model(X, theta) - y)**2)

# print(cost_function(X, y, theta))

# 3. Gradient descent
def grad(X, y, theta):
    m = len(y)
    return 1/m * X.T.dot(model(X, theta) - y)

def gradient_descent(X, y, theta, learning_rate, n_iterations):
    
    cost_history = np.zeros(n_iterations) # création d'un tableau de stockage pour enregistrer l'évolution du Cout du modele
    
    for i in range(0, n_iterations):
        theta = theta - learning_rate * grad(X, y, theta) # mise a jour du parametre theta (formule du gradient descent)
        cost_history[i] = cost_function(X, y, theta) # on enregistre la valeur du Cout au tour i dans cost_history[i]
        
    return theta, cost_history



# 4. Machine learning


n_iterations = 200
learning_rate = 0.1


theta_final, cost_history = gradient_descent(X, y, theta, learning_rate, n_iterations)
print('theta_final\n', theta_final)

predictions = model(X, theta_final)

# Display data into graphic
fig, axs = plt.subplots(2)
axs[0].scatter(x, y) # initial data
axs[0].plot(x, predictions, c='g') # model (from linear regression)
axs[1].plot(range(n_iterations), cost_history)
plt.show()


# Performances du model: R²
def coef_determination(y, pred):
    u = ((y - pred)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v
print(coef_determination(y, predictions))