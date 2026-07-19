import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    if not isinstance(x,np.ndarray):
        x=np.array(x)

    return np.where(x<0,0,x)