import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 
from std_msgs.msg import String

class Subs(Node):
    
    def __init__(self,t:int=0.5):
        super().__init__("SpiderSubs")
        self.subscription = self.create_subscription(String,"spider_topic",self.receiver,10)
        
        
    def receiver(self,msg):
        print(msg.data)
        
        

def main(args=None):
    rclpy.init(args=args)
    node = Subs()
    rclpy.spin(node)
    rclpy.shoutdown()

if __name__ == "__main__":
    print("starting...")
    main()
