import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 
from std_msgs.msg import String
import datetime 
from datetime import datetime

class Subs(Node):
    
    def __init__(self,t:int=0.5):
        super().__init__("SpiderSubs")
        self.subscription = self.create_subscription(Twist,"monitor",self.receiver,10)
        
        
    def receiver(self,msg):
        print("---------",str(datetime.now()))
        print("posição: ",msg.angular.x,"em x")
        print("posição: ",msg.angular.y,"em y")
        print("posição:" ,msg.angular.z,"em z")
        print("---------")
        

def main(args=None):
    rclpy.init(args=args)
    node = Subs()
    rclpy.spin(node)
    rclpy.shoutdown()

if __name__ == "__main__":
    print("starting...")
    main()
