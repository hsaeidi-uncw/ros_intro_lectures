#!/usr/bin/env python3

import rospy
# we are going to read turtlesim/Pose messages this time
from turtlesim.msg import Pose
#importing the new message from our package
from ros_intro_lectures.msg import Shortpose
# for radians to degrees conversions
import math

ROTATION_SCALE = 180.0/math.pi

pos_msg = Shortpose()

def pose_callback(data):
	global pos_msg
	# convert angular position to degrees
	pos_msg.theta = data.theta * ROTATION_SCALE
	# convert x and y to cm
	pos_msg.x = data.x * 100
	pos_msg.y = data.y * 100
	
	
if __name__ == '__main__':
	# initialize the node
	rospy.init_node('pos_publisher', anonymous = True)
	# add a subscriber to it to read the position information
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
	# add a publisher with a new topic using the Shortpos message
	pos_pub = rospy.Publisher('/turtle1/shortpose', Shortpose, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		# publish the message
		pos_pub.publish(pos_msg)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
	
