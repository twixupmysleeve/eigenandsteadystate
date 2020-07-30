# Relationship between the Eigenvectors of a 2x2 Stochastic Matrix and its Steady State Vector
While I was learning about Markov Chains and the idea of the "Steady State" of a system, it made me also reflect on the logic behind Eigenvectors. I realized that the logic between the Eigenvectors and Steady State Vectors was pretty similar. I was also simultaneously writing a program to see if I could observe some sort of a pattern when I multiplied a matrix to itself a certain number of times. 

I thought I'd ccombine the two ideas, so I wrote a program that will take in 2 inputs A and B (from 0 to 1), which will serve as the respective components for the first row of the Markov Matrix. C and D, the components of row 2, will be automatically be calculated by subtracting their respective upper components from 1. And then, sit back and watch as the program multiplies the probability matrix to itself 100 times in order to obtain its steady state vectors and normalises them. Next, it calculuates the Eigenvectors, normalises them, and plots a graph that shows:

1. The 2 Eigenvectors (normalised)
2. The Steady-State Vector
3. The Normalised Steady-State Vector

Note how the steady-state vector ALWAYS has the same (or directly opposite) direction as the Eigenvector, which, if you calculate, has the Eigenvalue of 1 (or closest to 1)

**I plan on updating this soon for a 3x3 Stochastic Matrix and soon an *n*x*n* (if that's possible)**
