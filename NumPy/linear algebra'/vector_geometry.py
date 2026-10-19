import numpy as np
import matplotlib.pyplot as plt

a = np.array([5,4,1])
b = np.array([4,5,2])
c = np.array([1,2,5])

dot_product_ab = np.dot(a,b)
print(dot_product_ab)
cos_theta_ab = dot_product_ab/(np.linalg.norm(a)*np.linalg.norm(b))
print(cos_theta_ab)
angle_ab = np.degrees(np.arccos(cos_theta_ab))
print(f"Angle between A and B : {angle_ab:.0f} degree")

ax = plt.figure().add_subplot(projection = '3d')
ax.quiver(0,0,0,*a)
ax.quiver(0,0,0,*b)
plt.show()