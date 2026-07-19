import numpy as np

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    if not isinstance(x,np.ndarray):
        x=np.array(x)

    f_x=np.where(x>0,x,alpha*(np.exp(x)-1))
    return f_x.tolist()