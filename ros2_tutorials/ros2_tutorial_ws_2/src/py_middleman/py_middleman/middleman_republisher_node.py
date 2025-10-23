import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MiddlemanRepublisher(Node):
    def __init__(self):
        super().__init__('middleman_republisher')
        self.i = 0

        self.subscription = self.create_subscription(
            String,
            'pub_topic',
            self.listener_callback,
            10
        )

        self.publisher_ = self.create_publisher(String, 'repub_topic',10)
        

    def listener_callback(self, msg):
        message = 'Received: "{0}"'.format(msg.data)
        self.get_logger().info(message)
        self.republisher_callback(msg)

    
    def republisher_callback(self,msg):
        new_msg = String()
        new_msg.data = (msg.data + ' - Republished!')
        self.publisher_.publish(new_msg)
        self.get_logger().info(('Publishing: "{0}"').format(new_msg.data))


def main(args = None):
    rclpy.init(args = args)
    middleman_republisher = MiddlemanRepublisher()
    rclpy.spin(middleman_republisher)

    middleman_republisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()