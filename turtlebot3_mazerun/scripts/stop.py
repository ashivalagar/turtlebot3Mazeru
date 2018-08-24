#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
#from std_msgs.msg import Int32

def callback(msg):
	print('=========================================================')
	print('s1 [270]')
	print msg.ranges[270]
	print('s2 [0]')
	print msg.ranges[0]
	print('s3 [90]')
	print msg.ranges[90]

	if msg.ranges[0]> 0.5:
		move.linear.x = 0.5
		move.angular.z = 0.0
	
	else:
		move.linear.x = 0.0
		move.angular.z = 0.0

	pub.publish(move)

rospy.init_node('obstacle_avoidance')
sub = rospy.Subscriber('/scan', LaserScan, callback)
#sub = rospy.Subscriber('/irleft_reading', Int32, callback0)
#sub = rospy.Subscriber('/irright_reading', Int32, callback1)
#sub = rospy.Subscriber('/ircenter_reading', Int32, callback2)
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()


rospy.spin()
