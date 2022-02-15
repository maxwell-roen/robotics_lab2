# import our basic homogenous transformations from problem 2.
# we don't use rot_y here.
from p2_sol import rot_x
from p2_sol import rot_z
from p2_sol import translate_x
from p2_sol import translate_y
from p2_sol import translate_z
import math
import numpy as np


def get_magnitude_of_3d_vec(vec):
	"""
	Helper function to calculate the magnitude of a 3d vector.
	Formula is sqrt(a^2 + b^2 + c^2)
	:param vec: A 3d vector. 
	:return: The magnitude of that vector.
	"""
	return math.sqrt(math.pow(vec[0], 2) + math.pow(vec[1], 2) + math.pow(vec[2], 2))


def H_1(v0):
	"""
	Transformation H_1 from problem 3.
	:param v0: an initial point
	:return v1: the updated position
	"""
	# follow the individual steps to create the single homogenous transformation
	# we use right multiplies as we are using moving frames.
	H = translate_x(2.5)
	H = np.matmul(H, translate_z(0.5))
	H = np.matmul(H, translate_y(-1.5))

	# Multiply H*v0 to get resulting point
	v1 = np.matmul(H, v0)

	return v1


def H_2(v0):
	"""
	Transformation H_2 from problem 3
	:param v0: an initial point
	:return v1: the updated position
	"""
	# follow the individual steps to create the single homogenous transformation
	# we use right multiplies as we are using moving frames.
	H = translate_z(0.5)
	H = np.matmul(H, translate_x(2.5))
	H = np.matmul(H, translate_y(-1.5))

	# Multiply H*v0 to get resulting point
	v1 = np.matmul(H, v0)

	return v1


def H_3(v0):
	"""
	Transformation H_3 from problem 3
	:param v0: an initial point
	:return v1: the updated position
	"""
	# follow the individual steps to create the single homogenous transformation
	# we use left multiplies as we are using a fixed frame.
	H = translate_x(2.5)
	H = np.matmul(translate_z(0.5), H)
	H = np.matmul(translate_y(-1.5), H)


	# Multiply H*v0 to get resulting point
	v1 = np.matmul(H, v0)

	return v1


def H_4(v0):
	"""
	Transformation H_4 from problem 3
	:param v0: an initial point
	:return v1: the updated position
	"""
	# follow the individual steps to create the single homogenous transformation
	# we use left multiplies as we are using a fixed frame.
	H = translate_z(0.5)
	H = np.matmul(translate_x(2.5), H)
	H = np.matmul(translate_y(-1.5), H)

	# Multiply H*v0 to get resulting point
	v1 = np.matmul(H, v0)

	return v1


def H_5(v0):
	"""
	Transformation H_5 from problem 3
	:param v0: an initial point
	:return v1: the updated position
	"""
	# follow the individual steps to create the single homogenous transformation
	# we use right multiplies as we are using moving frames.
	H = rot_x(math.pi / 2)
	H = np.matmul(H, translate_x(3))
	H = np.matmul(H, translate_z(-3))
	H = np.matmul(H, rot_z(-math.pi / 2))

	# multiple H*v0 to get the resulting point
	v1 = np.matmul(H, v0)

	return v1


if __name__ == '__main__':
	# declare a starting point
	v0 = [1, 1, 1]
	# append the magnitude to the vector so we can multiply by H, which will be 4x4
	v0.append(get_magnitude_of_3d_vec(v0))

	# set some numpy print options for the output. Suppress forces numpy to not use scientific notation
	# for small values.
	np.set_printoptions(precision=2, suppress=True)

	# test the H_1 transformation
	v1 = H_1(v0)
	# and this matches what we got by hand.
	print(v1)

	# test the H_2 transformation
	v2 = H_2(v0)
	# which matches our result from H_1 -- the first four transformations should have the same result, we're good to go.
	print(v2)

	# test the H_3 transformation
	v3 = H_3(v0)
	# again, good to go.
	print(v3)

	# test the H_4 transformation
	v4 = H_3(v0)
	# looks good.
	print(v4)

	# finally, test the H_5 transformation. gotta work this one by hand too.
	v5 = H_5(v0)
	# we are expecting to get: [6.2, 4.2, -1, sqrt(3)]. and we do.
	print(v5)
