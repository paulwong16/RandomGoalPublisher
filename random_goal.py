#!/usr/bin/env python
import rospy
import random
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatusArray

def callback(data):
    print data.status_list
    if data.status_list:
        if data.status_list[0].status == 3:

            client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
            client.wait_for_server()

            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = "map"
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = random.uniform(-10, 10)
            goal.target_pose.pose.position.y = random.uniform(-10, 10)
            goal.target_pose.pose.position.z = random.uniform(-10, 10)
            goal.target_pose.pose.orientation.w = 1.0;

            client.send_goal(goal)
            wait = client.wait_for_result()
            if not wait:
                rospy.logerr("Action server not available!")
                rospy.signal_shutdown("Action server not available!")
            else:
                return client.get_result()

    else:
        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        client.wait_for_server()

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = random.uniform(-10, 10)
        goal.target_pose.pose.position.y = random.uniform(-10, 10)
        goal.target_pose.pose.position.z = random.uniform(-10, 10)
        goal.target_pose.pose.orientation.w = 1.0;

        client.send_goal(goal)
        wait = client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return client.get_result()


def listener():
    rospy.init_node('random_goal_publisher', anonymous=True)
    print "init"
    rospy.Subscriber("move_base/status", GoalStatusArray, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
