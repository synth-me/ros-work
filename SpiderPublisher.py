import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import numpy as np
import time

class Publisher(Node):
    
    def __init__(self,t:int=0.5):
        super().__init__("SpiderPublisher")
        self.publisher = self.create_publisher(String,"spider_topic",10)
        self.timer = self.create_timer(t,self.msg)
        self.get_logger().info("loading....")
        return None

    def msg(self):
        msg_d=String()
        n = int(np.random.randint(20))
        msg_d.data = str(n)
        time.sleep(1)
        self.publisher.publish(msg_d)
        

def main(args=None):
    rclpy.init(args=args)
    node = Publisher()
    rclpy.spin(node)
    rclpy.shoutdown()

if __name__ == "__main__":
    print("starting...")
    main()

