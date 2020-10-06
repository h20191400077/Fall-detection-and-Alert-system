#!/usr/bin/env python
import rospy
import os
from std_msgs.msg import String

def Accelerometer():
	pub = rospy.Publisher('Acc_axes', String, queue_size = 10)
	rospy.init_node('Accelerometer', anonymous = True)
	rate = rospy.Rate(2)
	f = open("/home/ashutosh/catkin_ws/src/first_pkg/adl_walk_acc.txt", "rt")
	l = f.readline()
	while not rospy.is_shutdown() and l:
		hello_str = l
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()
		l = f.readline()

if __name__ == '__main__':
	Accelerometer()
