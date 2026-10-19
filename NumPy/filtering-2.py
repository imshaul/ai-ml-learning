import numpy as np
np1 = np.array([32,52,64,65,95,83,132])

filtered = []
# for filter in np1:
#     if filter % 2 == 0:
#         filtered.append(True)
#     else :
#         filtered.append(False)
# print(filtered)
# print(np1[filtered])

# instead we can do this

filtered = np1 % 2 == 0
print(np1[filtered])