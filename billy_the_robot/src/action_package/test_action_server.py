import time

import os

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


class TestActionServer(Node):

    def __init__(self):
        super().__init__('test_action_server')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'test',
            self.execute_callback)

    def execute_callback(self, goal_handle):

        os.system('cls||clear')

        self.get_logger().info('starting...')

        feedback_msg = Fibonacci.Feedback()

        feedback_msg.partial_sequence = []


        for i in range(0, goal_handle.request.order):

             while 1:
                print('pls enter number')
                answer = input()

                try:

                     number = int(answer)

                     feedback_msg.partial_sequence.append(number)

                     self.get_logger().info('feedback: {0}'.format(feedback_msg.partial_sequence))

                     goal_handle.publish_feedback(feedback_msg)

                     break
                except:
                     print('The variable is not a number')



        goal_handle.succeed()

        result = Fibonacci.Result()

        result.sequence = feedback_msg.partial_sequence

        print('done')

        return result


def main(args=None):

    os.system('cls||clear')

    print('waiting')

    rclpy.init(args=args)

    test_action_server = TestActionServer()

    rclpy.spin(test_action_server)


if __name__ == '__main__':
    main()
