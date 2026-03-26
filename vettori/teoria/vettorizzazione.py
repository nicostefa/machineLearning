import numpy as np
from timeit import Timer

matrix = np.arange(10)
print("matrix: ", matrix)

matrix = np.arange(1000000)
def loop_sum():
    return [val+1 for val in matrix]

def numpy_sum():
    return matrix + 1


exectime_loop = min(Timer(loop_sum).repeat(10,10))
exctime_num = min(Timer(numpy_sum).repeat(10,10))

print("exectime_loop: ", exectime_loop)
print("exctime_num: ", exctime_num)