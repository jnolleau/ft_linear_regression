from csvReader import Reader
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt


# Read the .csv file and get data as ndarray
rd = Reader()

if (len(sys.argv) > 1):
    rd.setFilename(sys.argv[1])

headers, mileage, prices = rd.getData()


# 1. model F
def model(X, theta):
    return X.dot(theta)

# 2. Fonction cout
def cost_function(X, y, theta):
    m = len(y)
    return 1/(2*m) * np.sum((model(X, theta) - y)**2)

# 3. Gradient descent
def grad(X, y, theta):
    m = len(y)
    return 1/m * X.T.dot(model(X, theta) - y)

def gradient_descent(X, y, theta, learningRate, n_iterations):
    
    cost_history = np.zeros(n_iterations)

    for i in range(0, n_iterations):
        theta = theta - learningRate * grad(X, y, theta)
        cost_history[i] = cost_function(X, y, theta)
    return theta, cost_history

def scaling(x):
    return x / max(x)

# 4. Machine learning

# matrice X ( où F = X . theta)
x = scaling(mileage)
X = np.hstack((x, np.ones(x.shape)))

# Vecteur parametres (theta0 theta1) initialisation a une valeur random
np.random.seed(0) # Pour avoir toujours le meme random
theta = np.random.randn(2,1)

learningRate = 1.0
n_iterations = 200
theta_final, cost_history = gradient_descent(X, prices, theta, learningRate, n_iterations)

# Display data into graphic
predictions = model(X, theta_final)

fig, axs = plt.subplots(1,2)
axs[0].scatter(mileage, prices) # initial data
axs[0].plot(mileage, predictions, c='tab:orange') # model (from linear regression)
axs[0].set_title("Raw data and trend line")
axs[0].set_xlabel(headers[0])
axs[0].set_ylabel(headers[1])
axs[1].plot(range(n_iterations), cost_history)
axs[1].set_title("Learning curve (Cost value / iteration)")
axs[1].set_xlabel("Number of iterations")
axs[1].set_ylabel("Cost")
plt.suptitle('ft_linear_regression')

# Save thetas into csv
out_headers = ['theta1', 'theta0', 'max']
out_theta = theta_final.flatten().tolist()
out_theta.append(max(mileage)[0].tolist())

np.set_printoptions(suppress=True)
print(f"theta0 = {theta_final[1]}\ntheta1 = {theta_final[0]}")

with open('theta.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(out_headers)
    writer.writerow(out_theta)


# Performances du model: R²
def coef_determination(y, pred):
    u = ((y - pred)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v
print('R² = ', coef_determination(prices, predictions))

plt.show()
