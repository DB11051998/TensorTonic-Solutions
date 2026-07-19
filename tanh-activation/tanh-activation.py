import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    if not isinstance(x,np.ndarray):
        x=np.array(x)

    return np.tanh(x)