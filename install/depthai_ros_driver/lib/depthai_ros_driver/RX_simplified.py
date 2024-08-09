#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image


class CamInfoSubscriber(Node):

    def __init__(self):
        super().__init__('cam_info_subscriber')
        
        self.subscription = self.create_subscription(
            Image,
            '/oak/rgb/image_raw',
            self.listener_callback_rgb_raw,
            10)

        self.subscription  # prevent unused variable warning

    def listener_callback_rgb_raw(self, msg):
        self.get_logger().info('Received RGB image raw')


def main(args=None):
    rclpy.init(args=args)

    cam_info_subscriber = CamInfoSubscriber()

    rclpy.spin(cam_info_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    cam_info_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()