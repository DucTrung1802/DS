from numba import jit, cuda
import numpy as np
# to measure exec time
from timeit import default_timer as timer 

BENCHMARK_PARAMETER = 200000000

# normal function to run on cpu
def func(a):							 
	for i in range(BENCHMARK_PARAMETER):
		a[i]+= 1	

# function optimized to run on gpu 
@jit(target_backend='cuda')						 
def func2(a):
	for i in range(BENCHMARK_PARAMETER):
		a[i]+= 1
		
if __name__=="__main__":
	n = BENCHMARK_PARAMETER						
	a = np.ones(n, dtype = np.float64)
	
	start = timer()
	func(a)
	print("without GPU:", timer()-start) 
	
	start = timer()
	func2(a)
	print("with GPU:", timer()-start)


