import rclpy
from rclpy.node import Node
from autoware_auto_vehicle_msgs.msg import GearReport, SteeringReport, VelocityReport

class NewSubscriber(Node):

    def __init__(self):
        super().__init__('new_subscriber')
        
        # Subscribers for the messages
        self.create_subscription(GearReport, 'gear_report_topic', self.gear_report_callback, 10)
        self.create_subscription(SteeringReport, 'steering_report_topic', self.steering_report_callback, 10)
        self.create_subscription(VelocityReport, 'velocity_report_topic', self.velocity_report_callback, 10)


    def gear_report_callback(self, msg):
        self.get_logger().info('Received GearReport Message')

    def steering_report_callback(self, msg):
        self.get_logger().info('Received SteeringReport Message')

    def velocity_report_callback(self, msg):
        self.get_logger().info('Received VelocityReport Message')

def main(args=None):
    rclpy.init(args=args)
    new_subscriber = NewSubscriber()
    rclpy.spin(new_subscriber)
    new_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()