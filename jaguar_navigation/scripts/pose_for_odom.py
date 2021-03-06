#!/usr/bin/env python
import rospy
import time
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped

pose_publisher = None

def odom_callback(msg):
    global pose_publisher
    msg_ = PoseWithCovarianceStamped()
    msg_.header.stamp = rospy.Time.now()
    msg_.pose = msg.pose
    msg_.header.frame_id = "odom"
    pose_publisher.publish(msg_)
    time.sleep(3)

if __name__ == '__main__':
    rospy.init_node('pose_from_odom')
    topic  = rospy.get_param('~odom_topic', 'odometry/filtered')
    rospy.Subscriber(topic, Odometry, odom_callback)
    pose_publisher = rospy.Publisher('pose', PoseWithCovarianceStamped, queue_size=1);
    rospy.spin()