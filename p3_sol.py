from p2_sol import rot_x
from p2_sol import rot_y
from p2_sol import rot_z
from p2_sol import translate_x
from p2_sol import translate_y
from p2_sol import translate_z
import math
import numpy as np

def H_1(v0):
	"""
	Transormation from from problem 3.
	"""
	# follow the invidivual steps to create the single homogenous transformation
	H = translate_x(2.5)
	H = np.matmul(H, translate_z(0.5))
	H = np.matmul(H, translate_y(-1.5))
	# multiply the initial vector by H to produce the result
	#v1 = H.dot(v0)
	# oh, it's supposed to be left multiply? I think? is that the issue?
	# idk, my linear algreba is weak/nonexistent, need to go learn that. let's try it though:
	#v1 = v0.dot(H)
	# that doesn't work. how about:
	v1 = np.matmul(v0, H)
	# that seems to be wrong, too. come back tomorrow;
	
	return v1


if __name__ == '__main__':
    v0 = [0, 0, 0, 0]
    v1 = H_1(v0)
    print(v1)

