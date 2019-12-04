import numpy as np

x=np.array([1, 2, 3])
x_=np.zeros(len(x))
z_=np.zeros(len(x))

for i in range(len(x)):
    z_[i]=x[i]+1
    z_[i]=z_[i]+1
    x_[i]=x[i]+3
    print(x[i])
    print(z_[i])
    print(x_[i])
    

    
