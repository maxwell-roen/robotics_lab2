import rbm
import numpy as np
import math


def calculate_fixed_frame_roll_pitch_yaw_rotation(starting_pt, psi, theta, phi):
	"""
	This function calculates the results of a roll-pitch-yaw rotation based on the given angles.
	:param starting_pt: The initial position
	:param psi: Rotation about x, the roll
	:param theta: Rotation about y, the pitch
	:param phi: Rotation about z, the yaw
	:return: A vector containing the new position of the point after the rotations.
	"""
	# create the three rotation matrices using the rotation matrix formulas defined in the rbm module
	Rx = rbm.rot_x(psi)
	Ry = rbm.rot_y(theta)
	Rz = rbm.rot_z(phi)

	# do two left multiplications to calculate the total rotation with a fixed frame
	H = np.matmul(Rz, (np.matmul(Ry, Rx)))

	# then calculate the result
	updated_pt = np.matmul(H, starting_pt)

	return updated_pt


if __name__ == '__main__':
	# rotation values from the problem statement:
	theta = math.pi / 2
	phi = math.pi / 2
	psi = math.pi / 2

	# a simple test case.
	v0 = [1, 1, 1]
	v1 = calculate_fixed_frame_roll_pitch_yaw_rotation(v0, theta, phi, psi)
	# based on doing this by hand, we expect to get [1, 1, -1], and we do.
	print(f'Result:\n{v1}\n')

	# another example
	v0 = [2, 4, 6]
	v1 = calculate_fixed_frame_roll_pitch_yaw_rotation(v0, theta, phi, psi)
	# based on doing this by hand, we expect this to give [6, 4, -2], and we do.
	print(f'Result:\n{v1}')
