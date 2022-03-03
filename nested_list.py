### append
l = [[0,1],[2,3]]
 
flatten_list = []
 
for subl in l:
    for item in subl:
        flatten_list.append(item)
 
print(flatten_list)

### list comprehension
l = [[0,1], [2,3]]
 
flatten_list = [item for subl in l for item in subl]
 
print(flatten_list)

### deep flattening
from iteration_utilities import deepflatten
 
multi_depth_list = [[0,1], [[5]], [6,4]]
 
flatten_list = list(deepflatten(multi_depth_list))
 
print(flatten_list)

### itertools
import itertools
 
List_1 = [[1,2,3],[4,5,6],[7,8,9]] #List to be flattened
 
List_flat = list(itertools.chain(*List_1))
 
print(List_flat)

### reduce
from functools import reduce
 
multi_depth_list = [[3,2,1],[1,4,5]]
 
reduce(list.__add__, (list(items) for items in multi_depth_list

### numpy ravel
import numpy as np
 
list1 = np.array([[3,2,1], [4,5,6], [7,8,9]])
out = list1.ravel()
print(out)
                      

### numpy flatten
import numpy as np
 
lst = np.array([[3,2,1], [4,5,6], [7,8,9]])
out = lst.flatten()
print(out)
                      
             
### numpy reshape
import numpy as np
 
lst = np.array([[3,2,1], [4,5,6], [7,8,9]])
 
out = lst.reshape(-1)
 
print(out)
                      

### numpy flat
import numpy as np
 
lst = np.array([[3,2,1], [4,5,6], [7,8,9]])
 
print(list(lst.flat))
                      

### numpy concatenate
import numpy as np
 
lst = np.array([[3,2,1], [4,5,6], [7,8,9]])
 
print(list(numpy.concatenate(lst)))
                      

### lambda
flatten = lambda x: [i for row in x for i in row]
lst = [[3,2,1], [4,5,6], [7,8,9]]
out = flatten(lst)
print(out)
                      

### sum
l = [[1, 2, 3], [4, 5], [6]]
l = sum(l, [])
print(l)
                      

### reduce and concat
import functools
import operator
 
def functools_reduce(a):
    return functools.reduce(operator.concat, a)
l = [[1, 2, 3], [4, 5], [6]]
print(functools_reduce(l))
                      

### pandas flatten
from pandas.core.common import flatten
l = [[1,2,3], [4,5], [6]]
print(list(flatten(l)))
                      

### matplotlib flatten
from matplotlib.cbook import flatten
l = [[1,2,3], [4,5], [6]]
print(list(flatten(l)))
                      
                      
### django flatten
from django.contrib.admin.utils import flatten
l = [[1,2,3], [4,5], [6]]
print(flatten(l))
