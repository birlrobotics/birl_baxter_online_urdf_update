#!/usr/bin/env python

import rospy
from baxter_core_msgs.msg import URDFConfiguration
import os

dir_of_this_script = os.path.dirname(os.path.realpath(__file__))

def main():
    rospy.init_node('pub_urdf', anonymous=True)
    pub = rospy.Publisher('/robot/urdf', URDFConfiguration, queue_size=100)
    msg = URDFConfiguration()
    
    now = rospy.Time.now()
    msg.time.secs = now.secs
    msg.time.nsecs = now.nsecs
    
    msg.link = "right_hand"
    msg.joint = "right_gripper_base"

    msg.urdf = open(os.path.join(dir_of_this_script, 'update_urdf.xml'), 'r').read()

    print msg

    pub.publish(msg)


if __name__ == '__main__':
    main()
