import numpy as np
ages = np.array([[23,52,12,18,20],
                [39,80,15,27,53]])
teenagers = ages[ages<18] # under 18
adult = ages[(ages>=18) & (ages<50)] # in between 18 and 50
senior = ages[ages>50]
even = ages[ages%2==0]
odd = ages[ages%2!=0]
print(ages[:,3])
print(odd)
print(even)
print(adult)
print(senior)
print(teenagers)
# This is slow so we will use boolean indexing
adults = np.where(ages>=18, ages,"UA") # replaced with fill value (condition,array,fill value)
print(adults)
# slicing
single_array = np.array([23,52,12,18,20])
print(single_array[1:4]) # 4 is excluded here
print(single_array[-1])
# stacking 
a = np.arange(6).reshape(3,2)
b = np.arange(10,12).reshape(10,10)
print(a)
print(b)