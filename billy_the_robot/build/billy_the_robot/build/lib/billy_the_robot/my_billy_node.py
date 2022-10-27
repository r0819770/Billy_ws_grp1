#!/usr/bin/env python3
import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("minimal_publisher") #node name
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5
        self.create_timer(timer_period, self.timer_callback)
        self.i = 0
    
    def timer_callback(self):
        msg = String()
        msg.data = 'hello: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing: %s" % msg.data)
        self.i += 1 #aftellen

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node) #spin -> loop run
    node.destroy_node()
    rclpy.shutdown() #destroy node

if __name__ == '__main__':
    main()
