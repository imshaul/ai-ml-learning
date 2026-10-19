import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
new_arr = arr.reshape(5,2)
print(new_arr)
multi_dim = np.array([[43,65,85],
                    [32,73,23]])
print(multi_dim.flatten())