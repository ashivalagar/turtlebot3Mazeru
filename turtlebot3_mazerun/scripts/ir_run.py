#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32

def irrun():

	def callback2(msg):
		print('=====================================================')
		print ('irmid')
		print msg.data
		if msg.data < 100 :
			move.linear.x = 0.0
			rospy.sleep(2)
			
			
			def callback0(msg):
				print ('irleft')
				print msg.data
	
				if msg.data < 100 :
					def callback1(msg):
						print ('irright')
						print msg.data
						if msg.data > 100 :
							t0 = rospy.Time.now().to_sec()
							current_angle = 0
							while(current_angle < 1.57) :
								move.angular.z = -0.8
								t1 = rospy.Time.now().to_sec()
								current_angle = 0.8*(t1-t0)
								pub.publish(move)
								rospy.sleep(2)
							move.angular.z = 0.0
							rospy.sleep(1)



						else :
							t0 = rospy.Time.now().to_sec()
							current_angle = 0
							while(current_angle < 1.57) :
								move.angular.z = 0.8
								t1 = rospy.Time.now().to_sec()
								current_angle = 0.8*(t1-t0)
								pub.publish(move)
								rospy.sleep(2)
							move.angular.z = 0.0
							rospy.sleep(1)


					sub = rospy.Subscriber('/irright_reading', Int32, callback1)


		
				else :
					t0 = rospy.Time.now().to_sec()
					current_angle = 0
					while(current_angle < 1.57) :
						move.angular.z = 0.8
						t1 = rospy.Time.now().to_sec()
						current_angle = 0.8*(t1-t0)
						pub.publish(move)
						rospy.sleep(2)

				move.angular.z = 0.0
				pub.publish(move)
				rospy.sleep(1)
	
	
	
			sub = rospy.Subscriber('/irleft_reading', Int32, callback0)	
						
		else:
			move.linear.x = -0.5
			pub.publish(move)
			rospy.sleep(2)

		
	
	
	
		
	rospy.init_node('ir_run')
	

	sub = rospy.Subscriber('/irmid_reading', Int32, callback2)



	pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
	move = Twist()


	rospy.spin()


if __name__ == '__main__' :
	try:
		irrun()

	except rospy.ROSInterruptException:
		pass
