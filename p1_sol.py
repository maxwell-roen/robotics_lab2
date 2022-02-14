import rbm
import numpy as np
import math


# not sure if this is correct.
# FIXED FRAME -- should be left multiplies
if __name__ == '__main__':
	# declare values for x, y, and z rotations
	theta = math.pi / 2
	phi = math.pi / 2
	psi = math.pi / 2
	# declare a starting point, vector v0
	v0 = rbm.vec(1, 1, 1)
	# create the three rotation matrices using the rotation matrix formulas defined in the rbm module
	Rx = rbm.rot_x(psi)
	Ry = rbm.rot_y(theta)
	Rz = rbm.rot_z(phi)
	# do two right multiplications to calculate the total rotation with moving frames
	R = np.matmul(Rx, Ry)
	R = np.matmul(R, Rz)
	# then calculate and display the results
	v1 = R.dot(v0)
	print(f'Result:\n{v1}')
