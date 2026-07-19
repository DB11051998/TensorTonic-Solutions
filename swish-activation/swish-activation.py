import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    if not isinstance(x,np.ndarray):
        x=np.array(x)

    sigm_x=1/(1+np.exp(-x))

    return x*sigm_x