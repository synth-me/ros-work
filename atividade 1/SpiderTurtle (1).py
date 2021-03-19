import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 
from std_msgs.msg import String
import time 
from datetime import datetime , timedelta
import sys

global state 
global position_state
state = []
position_state = [] 

class SpiderTurtle(Node):
    
    def __init__(self,t:int=1):
        super().__init__("SpiderTurle")
        self.publisher = self.create_publisher(Twist,"turtle1/cmd_vel",10)
        self.publisher_monitor = self.create_publisher(Twist,"monitor",10)
        self.timer = self.create_timer(t,self.msg)
        self.get_logger().info("loading....")
        return None
    
    def ahead(self,ml,ma):
        ml.x = 0.0
        ml.y = 1.0
        ml.z = 0.0
            
        ma.x = 0.0
        ma.y = 1.0
        ma.z = 0.0
        return True 
        
    def circulo(self,ml,ma):
        ml.x = 1.0
        ml.y = 1.0
        ml.z = 1.0
            
        ma.x = 1.5
        ma.y = 1.5
        ma.z = 1.5
        return True
    
    def msg(self):
        msg_d=Twist()
        ml = msg_d.linear 
        ma = msg_d.angular
        
        if len(position_state) >= 3:
            print("---------",str(datetime.now()))
            print("iniciando circulo")
            self.circulo(ml,ma)
            state.append(1)
            self.publisher.publish(msg_d)
            self.publisher_monitor.publish(msg_d)
            if len(state) > 5:
                print("finished")
                print("é tetra , é tetra....")
                sys.exit() 
            time.sleep(4)
            print(len(state)-1,"segundo(s)")
            print("---------")
            
            state.append(1)
        elif len(position_state) <= 3 and len(state) < 1 :
            print("---------",str(datetime.now()))
            print("inciando reta")
            self.ahead(ml,ma)
            self.publisher.publish(msg_d)
            self.publisher_monitor.publish(msg_d)
            position_state.append(1)
            print(len(position_state),"segundo(s)")
            print("---------")
            time.sleep(3)
        else:
            pass
            
        
def main(args=None):
    rclpy.init(args=args)
    node = SpiderTurtle()
    rclpy.spin(node)
    rclpy.shoutdown()

if __name__ == "__main__":
    print("starting...")
    main()
