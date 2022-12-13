import cvxpy as cv
import numpy as np
import time
import matplotlib.pyplot as plt

SIZE = 100


def linear_system_cvxpy(n: int):
    start = time.time()
    variables = cv.Variable(n)
    constraints = []
    a = np.random.randint(SIZE, size=(n, n))
    b = np.random.randint(SIZE, size=n)

    for i in range(n):
        constraint = sum(a_i * x_i for a_i, x_i in zip(a[i], variables)) == b[i]
        constraints.append(constraint)

    objective = cv.Minimize(sum(x_i ** 1 for x_i in variables))
    problem = cv.Problem(objective, constraints)
    problem.solve()
    end = time.time()
    return end - start


def linear_system_numpy(n: int):
    start = time.time()
    a = np.random.randint(SIZE, size=(n, n))
    b = np.random.randint(SIZE, size=n)
    np.linalg.solve(a, b)
    end = time.time()
    return end - start


l_cvx = []
l_num = []
for i in range(1, 100):
    l_num.append(linear_system_numpy(i))
    l_cvx.append(linear_system_cvxpy(i))

plt.plot(l_num, 'g', l_cvx, 'r')
plt.xlabel("number of variables")
plt.ylabel("time (in sec)")
plt.legend(["numpy", "cxvpy"])
plt.figure(figsize=(8,10))
plt.show()
