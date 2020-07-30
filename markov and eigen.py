import numpy as np
import matplotlib.pyplot as plt
import math
import time

print("Please input A and B (both between 0 and 1) for a stochastic matrix: \n",
      np.array([["A", "B"], ["C", "D"]]))
print("where the values of C and D will automatically be calculated based on the input")

x = float(input("A: "))
y = float(input("B: "))
p = 1 - x
q = 1 - y

a = np.array([[x, y], [p, q]])
b, b1, b2, b3, b4 = [], [], [], [], []
c = a

print("The input Stochastic Matrix is:\n", a)

for i in range(100):
    if i != 0:
        c = c.dot(a)
    b.append(i)
    b1.append(c[0][0])
    b2.append(c[0][1])
    b3.append(c[1][0])
    b4.append(c[1][1])

leng = math.sqrt(b1[-1]**2 + b3[-1]**2)

print("The steady-state vector of your Markov Matrix is:\n", np.array([[b1[-1]], [b3[-1]]]))
print("The normalized steady-state vector for your Markov Matrix is:\n", np.array([[b1[-1]/leng], [b3[-1]/leng]]))

val, vec = np.linalg.eig(a)

eig1 = plt.arrow(0, 0, vec[0][0], vec[1][0], head_width=0.05, length_includes_head=True, width=0.01)
eig2 = plt.arrow(0, 0, vec[0][1], vec[1][1], head_width=0.05, length_includes_head=True, width=0.01,
          label='Eigenvectors')
nssv = plt.arrow(0, 0, b1[-1]/leng, b3[-1]/leng, color="red", head_width=0.03, width=0.009,
          length_includes_head=True, linestyle='--', label='Normalized Steady State Vector')
ssv = plt.arrow(0, 0, b1[-1], b3[-1], color="green", head_width=0.02, width=0.006,
          length_includes_head=True, linestyle='-.', label='Steady State Vector')

plt.xlim(-1, 1)
plt.ylim(-1, 1)

plt.title("Relationship between Eigenvectors and Steady State Vector\n of a 2x2 Stochastic Matrix")

plt.legend([eig1, nssv, ssv],["Eigenvectors", "Normalised Steady-State Vector", "Steady-State Vector"])
plt.grid()

time.sleep(0.2)

plt.show()
