#!/usr/bin/env python
import rospy
import os
from std_msgs.msg import String

def Arduino():
	pub = rospy.Publisher('Fall_class', String, queue_size = 10)
	rospy.init_node('Arduino', anonymous = True)
	rospy.Subscriber('Magnitudes', String, Arduino)
	rate = rospy.Rate(2)
	f = open("/home/ashutosh/catkin_ws/src/first_pkg/classify_random.txt", "rt")
	l = f.readline()
	while not rospy.is_shutdown() and l:
		hello_str = l
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()
		l = f.readline()



if __name__ == '__main__':
	Arduino()
