#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import String

def callback(data):
	pub = rospy.Publisher('Magnitudes', String, queue_size = 10)
	rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
	f = open('/home/ashutosh/catkin_ws/src/first_pkg/gyro_out.txt', 'at')
	[a, b, c] = data.data.split()
	d = (float(a) * float(a)) + (float(b) * float(b)) + (float(c) * float(c))
	e = math.sqrt(d)
	f.write(str(e) + str('\n'))
	f.close()

def Gyro_class():
	rospy.init_node('Gyro_class', anonymous = True)
	rospy.Subscriber('Gyro_axes', String, callback)
	rospy.spin()
if __name__ == '__main__':
	Gyro_class()
	
