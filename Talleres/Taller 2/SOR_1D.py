import numpy as np

def sor_solver(A, b, omega, initial_guess, convergence_criteria):
    phi = initial_guess[:]
    residual = np.linalg.norm(np.matmul(A, phi) - b)
    while residual > convergence_criteria:
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i][j] * phi[j]
            phi[i] = (1 - omega) * phi[i] + (omega / A[i][i]) * (b[i] - sigma)
        residual = np.linalg.norm(np.matmul(A, phi) - b)
        print('Residual: {0:10.6g}'.format(residual))
    return phi


residual_convergence = 1e-16
omega = 0.5

A = np.array([[1,-8,-2],
              [1,1,5],
              [3,-1,1]])

b = np.array([1, 4, -2])

initial_guess = np.zeros(3)

phi = sor_solver(A, b, omega, initial_guess, residual_convergence)
print(phi)