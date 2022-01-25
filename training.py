from reader import Reader
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)
print(data)
x = data[:, 0]
y = data[:, 1]
x = x.reshape(x.shape[0], 1)
y = y.reshape(y.shape[0], 1)
print(x.shape)
print(y.shape)

def scaling(x):
    return x / max(x)

# Get data from list of tuple [[x,y]] to to list [x] and [y] 
def getColumns(data_list):
    mileage = []
    price = []
    headers = []
    pos = 0
    for lst in data_list:
        if (pos == 0):
            headers = data_list[0]
        else:
            mileage.append(float(lst[0]))
            price.append(float(lst[1]))
        pos+=1
    return headers

# read a csv file
reader = Reader()

if (len(sys.argv) > 1):
    reader.setFilename(sys.argv[1])

data_list = reader.getData()
headers = getColumns(data_list)

mileage = scaling(x)
price = y
# mileage = mileage.reshape(mileage.shape[0], 1)
# price = price.reshape(price.shape[0], 1)

# debug: print csv data into terminal
print(mileage.shape)
print(price.shape)

# matrice X ( où F = X . theta)
X = np.hstack((mileage, np.ones(mileage.shape)))
# np.set_printoptions(suppress=True)
# print(X.shape)
# print(mileage)

# Vecteur parametres (theta0 theta1) initialisation
# np.random.seed(0)
theta = np.random.randn(2,1)
# theta = np.array([-0.02145, 8499.5996]) # ------> form debug
# theta = theta.reshape(theta.shape[0], 1)
# print(theta.shape)
# print(theta)

# 1. model F
def model(X, theta):
    return X.dot(theta) 

# print(model(X, theta))

# 2. Fonction cout
def cost_function(X, y, theta):
    m = len(y)
    return 1/(2*m) * np.sum((model(X, theta) - y)**2) ### WHY ???

# print(cost_function(X, price, theta))

# 3. Gradient descent
def grad(X, y, theta):
    m = len(y)
    return 1/m * X.T.dot(model(X, theta) - y)

def gradient_descent(X, price, theta, learningRate, n_iterations):
    
    cost_history = np.zeros(n_iterations)

    for i in range(0, n_iterations):
        theta = theta - learningRate * grad(X, price, theta)
        cost_history[i] = cost_function(X, y, theta)
        # print(theta)
    return theta, cost_history

# 4. Machine learning
learningRate = 1.0
n_iterations = 200
theta_final, cost_history = gradient_descent(X, price, theta, learningRate, n_iterations)
print(theta_final)

# Display data into graphic
predictions = model(X, theta_final)

fig, axs = plt.subplots(2)
axs[0].scatter(x, price) # initial data
axs[0].plot(x, predictions, c='g') # model (from linear regression)
plt.xlabel(headers[0])
plt.ylabel(headers[1])
plt.title('ft_linear_regression')
axs[1].plot(range(n_iterations), cost_history)
plt.show()


# Save thetas into csv
out_headers = ['theta1', 'theta0']
theta_final[0][0] = theta_final[0][0] / max(x)

with open('theta.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(out_headers)
    writer.writerow(theta_final.flatten())


# Performances du model: R²
def coef_determination(y, pred):
    u = ((y - pred)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v
print('R² = ', coef_determination(y, predictions))