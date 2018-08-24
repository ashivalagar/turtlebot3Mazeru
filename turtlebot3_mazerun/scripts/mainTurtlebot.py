#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32

mode = "IR"  # LDS or IR
irFront = 0
irLeft = 0
irRight = 0
ldsFront = 0
ldsLeft = 0
ldsRight = 0

movLimit = 30


def callbackLDS(msg):
    global ldsFront
    global ldsLeft
    global ldsRight
    ldsFront = msg.ranges[0]
    ldsLeft = msg.ranges[90]
    ldsRight = msg.ranges[270]


def movABlk():
    move.linear.x = -0.22
    move.angular.z = 0.0
    pub.publish(move)
    if mode == "IR":
        rospy.sleep(0.4)
        brake()


def movLeft():
    move.linear.x = 0.0
    move.angular.z = 1.57
    pub.publish(move)
    rospy.sleep(1)
    brake()


def movRight():
    move.linear.x = 0.0
    move.angular.z = -1.57
    pub.publish(move)
    rospy.sleep(1)
    brake()


def movOneEighty():
    move.linear.x = 0.0
    move.angular.z = -1.57
    pub.publish(move)
    rospy.sleep(2)


def brake():
    move.linear.x = 0.0
    move.angular.z = 0.0
    pub.publish(move)
    rospy.sleep(1)


def callbackirFront(msg):
    global irFront
    irFront = msg.data
    print(irFront)


def callbackirLeft(msg):
    global irLeft
    irLeft = msg.data
    print(irLeft)


def callbackirRight(msg):
    global irRight
    irRight = msg.data


if __name__ == '__main__':
    rospy.init_node('mainTurtlebot')
    sub = rospy.Subscriber('/scan', LaserScan, callbackLDS)
    sub = rospy.Subscriber('/irmid_reading', Int32, callbackirFront)
    sub = rospy.Subscriber('/irright_reading', Int32, callbackirRight)
    sub = rospy.Subscriber('/irleft_reading', Int32, callbackirLeft)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    global movCounter
    global move
    movCounter = 0
    move = Twist()

    while not rospy.is_shutdown():

        print('=========================================================')

        if (mode == "IR") and (movCounter <= movLimit):
            print("+++")
            print("IR front reading: ", irFront)
            print("IR left reading: ", irLeft)
            print("IR right reading: ", irRight)
            print("+++")

            movCounter += 1
            if irFront >= 45:
                print("Action: Move forward")
                movABlk()
            else:
                if irLeft >= 45:
                    print("Action: Turn right")
                    movLeft()
                elif irRight >= 45:
                    print("Action: Turn left")
                    movRight()
                elif (irRight <= 40) and (irLeft <= 40):
                    print("Action: Turn 180")
                    movOneEighty()

        elif mode == "LDS":
            print("+++")
            print("LDS front: ", ldsFront)
            print("LDS left: ", ldsLeft)
            print("LDS right: ", ldsRight)
            print("+++")

            if (ldsFront > 0.2) or (ldsFront == 0.0):
                print("Action: Move forward")
                movABlk()
            else:
                brake()
                if ldsLeft > 0.15:
                    print("Action: Turn right")
                    movLeft()
                elif ldsRight > 0.15:
                    print("Action: Turn left")
                    movRight()
                elif (ldsLeft < 0.15) and (ldsRight < 0.15):
                    print("Action: Turn 180")
                    movOneEighty()

        # rospy.spin()
        rate.sleep()
