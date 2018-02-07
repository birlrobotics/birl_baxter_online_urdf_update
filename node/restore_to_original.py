#!/usr/bin/env python

import rospy
from baxter_core_msgs.msg import URDFConfiguration
import os

dir_of_this_script = os.path.dirname(os.path.realpath(__file__))

def main():
    rospy.init_node('pub_urdf', anonymous=True)
    pub = rospy.Publisher('/robot/urdf', URDFConfiguration, queue_size=0, latch=True)
    msg = URDFConfiguration()
    
    now = rospy.Time.now()
    msg.time.secs = now.secs
    msg.time.nsecs = now.nsecs
    
    msg.link = "right_hand"
    msg.joint = "right_gripper_base"

    msg.urdf = open(os.path.join(dir_of_this_script, 'original.xml'), 'r').read()

    rospy.sleep(3)
    pub.publish(msg)

if __name__ == '__main__':
    main()
