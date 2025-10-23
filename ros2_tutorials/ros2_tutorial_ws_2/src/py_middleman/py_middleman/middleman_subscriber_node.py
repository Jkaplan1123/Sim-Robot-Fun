import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MiddlemanSubscriber(Node):

    def __init__(self):
        super().__init__('middleman_subscriber')
        self.subscription = self.create_subscription(
            String,
            'repub_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, new_msg):
        self.get_logger().info('I heard: "%s"' % new_msg.data)


def main(args=None):
    rclpy.init(args=args)

    middleman_subscriber = MiddlemanSubscriber()

    rclpy.spin(middleman_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    middleman_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()