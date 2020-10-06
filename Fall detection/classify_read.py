#!/usr/bin/env python
import rospy
import math
from datetime import datetime
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
	f = open('/home/ashutosh/catkin_ws/src/first_pkg/classify_output.txt', 'at')
	[a, b] = data.data.split()
	d = float(a)
	e = float(b)
	dt = datetime.now()
	if (d >= 0.91 and d <= 1.00) and (e >= 9.6 and e <= 21.6):
		f.write(str(dt) + str('\t') + str("Back fall ") + str('\n'))
	elif (d >= 0.94 and d <= 1.28) and (e >= 38.0 and e <= 67):
		dt = datetime.now()
		f.write(str(dt) + str('\t') + str("Walking ") + str('\n'))
	elif (d >= 0.91 and d <= 0.94) and (e >= 2.63 and e <= 5.5):
		dt = datetime.now()
		f.write(str(dt) + str('\t') + str("Left fall ") + str('\n'))
	elif (d >= 0.9 and d <= 1.08) and (e >= 4.7 and e <= 22.45):
		dt = datetime.now()
		f.write(str(dt) + str('\t') + str("Right fall ") + str('\n'))
	elif (d >= 0.9 and d <= 0.97) and (e >= 1.1 and e <= 7.4):
		dt = datetime.now()
		f.write(str(dt) + str('\t') + str("Forward fall ") + str('\n'))

	f.close()

def Final_fall():
	rospy.init_node('Final_fall', anonymous = True)
	rospy.Subscriber('Fall_class', String, callback)
	
	rospy.spin()
if __name__ == '__main__':
	Final_fall()
	
