#! /usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist



def callback(msg):
	print('=========================================================')
	print('s1 [270]')
	print msg.ranges[270]
	print('s2 [0]')
	print msg.ranges[0]
	print('s3 [90]')
	print msg.ranges[90]

	if msg.ranges[0] > 0.5:
		move.linear.x = 0.5
		move.angular.z = 0.0
		pub.publish(move)

		
	else :
		move.linear.x = 0.0
		move.angular.z = 1.57

rospy.init_node('obstacle_avoidance')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
move = Twist()


rospy.spin()
		
