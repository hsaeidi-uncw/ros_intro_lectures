#!/usr/bin/env python3

import rospy
# we are going to read turtlesim/Pose messages this time
from turtlesim.msg import Pose
# for radians to degrees conversions
import math

ROTATION_SCALE = 180.0/math.pi


def pose_callback(data):
	# convert angular position to degrees
	rot_in_degree = data.theta * ROTATION_SCALE
	# convert x and y to cm
	x_in_cm = data.x * 100
	y_in_cm = data.y * 100
	# show the results
	rospy.loginfo("x is %0.2f cm, y is %0.2f cm, theta is %0.2f degrees", x_in_cm, y_in_cm, rot_in_degree)
	

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('pos_converter', anonymous = True)
	# add a subscriber to it to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
	
