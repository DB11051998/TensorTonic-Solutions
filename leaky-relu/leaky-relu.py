import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
   
     # Write code here
    if not isinstance(x,np.ndarray):
        x= np.array(x,dtype=np.float32)
    f_x=np.where(x<0,alpha*x,x)
    # f_x= x if x>=0 else alpha*x
    
    return f_x