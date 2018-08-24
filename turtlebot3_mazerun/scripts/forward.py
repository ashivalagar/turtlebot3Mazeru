#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def forward(msg):
	i = 0

	while i < 200:
		move.linear.x = 0.22
		pub.publish(move)
		i = i + 1

	move.linear.x = 0.0
	pub.publish(move)

	rospy.sleep(3)

rospy.init_node('forward')


pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
move = Twist()

rospy.spin()


if __name__ == '__main__' :
	try:
		forward(msg)

	except rospy.ROSInterruptException:
		pass
