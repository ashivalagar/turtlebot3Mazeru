#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def left(msg):
	t0 = rospy.Time.now().to_sec()
	current_angle = 0
	
	while(current_angle < 1.57) :
		move.angular.z = -0.8
		t1 = rospy.Time.now().to_sec()
		current_angle = 0.8*(t1-t0)
		pub.publish(move)
		rospy.sleep(2)
		
	
	

rospy.init_node('left')


pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
move = Twist()

rospy.spin()


if __name__ == '__main__' :
	try:
		left(msg)

	except rospy.ROSInterruptException:
		pass
