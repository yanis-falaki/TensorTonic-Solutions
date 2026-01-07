import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here

    x = np.array(X)

    if x.ndim < 2 or x.shape[0] < 2:
        return None

    mu = x.mean(axis=0)

    x_centered = x - mu

    cov = (x_centered.T @ x_centered) * (1/(x.shape[0] - 1))

    return cov