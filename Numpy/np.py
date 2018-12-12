import numpy as np

""" example 1 """
a = np.array([1,2,3,4,5])
a[a > 2] = 99
print(a) # [1 2 99 99 99] 


""" example 2 """
a2 = np.array([1,2,3,4,5])
a2_bool = a2 > 2
a2[a2_bool] = 99
print(a2) #[1 2 99 99 99]


""" example 3 """
c = np.array([[1,2,3],
              [1,2,3],
              [1,2,3]])

c[c[:,1] > 2, 1] = 99
print(c)

"""
[[1 2 3]
 [4 99 6]
 [7 99 9]]
"""

"""
bool = array[:, column_for_comparison] == value_for_comparison
array[bool, column_for_assignment] = new_value

array[array[:, column_for_comparison] == value_for_comparison, column_for_assignment] = new_value
"""