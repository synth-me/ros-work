import rclpy
from rclpy.node import Node


def MyNode():
    rclpy.init()
    node = Node("my_node")
    node.get_logger().info("the spider is jumping...")
    rclpy.spin(node)
    rclpy.shoutdown()

if __name__ == "__main__":
    print("starting...")
    MyNode()
