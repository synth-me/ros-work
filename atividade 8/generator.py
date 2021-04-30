import sys

def code_itself(a,b,c):
    code = """
import rclpy
import rclpy.node import Node

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range
import time

def sensor0():
    global sensor_solo_esq
    sensor_solo_esq = msg.range
    node.get_logger().info("gs0 "+str(sensor_solo_esq))

def sensor1():
    global sensor_solo_meio
    sensor_solo_meio = msg.range
    node.get_logger().info("gs1 "+str(sensor_solo_meio))


def sensor2():
    global sensor_solo_dir
    sensor_solo_dir = msg.range
    node.get_logger().info("gs2 "+str(sensor_solo_dir))

def move():
    msg = Twist()

    if sensor_solo_meio > {q1} :
        msg.linear.x = {q2}
        msg.angular.z = {q3}
        publisher.publish(msg)

    elif sensor_solo_esq > {q1} :
        msg.linear.x = {q2}
        msg.angular.z = {q3}
        publisher.publish(msg)

    elif sensor_solo_dir > {q1} :
        msg.linear.x = {q2}
        msg.angular.z = {q3}
        publisher.publish(msg)

rclpy.init()
node = Node("Seguidor_de_Linha")
node.get_logger().info("Executando um No Seguidor de Linha")
publisher = node.create_publisher(Twist,'/cmd_vel',10)
node.create_subscription(Range,'/gs0',sensor0,10)
node.create_subscription(Range,'/gs1',sensor1,10)
node.create_subscription(Range,'/gs2',sensor2,10)

sensor_solo_esq = sensor_solo_meio = sensor_solo_dir = 0
node.create_timer(0.01,move)

rclpy.spin(node)
rclpy.shutdown()

    """.format(q1=a,q2=b,q3=c)
    return code


def genCode(a,b,c):
    code = code_itself(a,b,c)
    file1 = open("arquivo_gerador.py","w")
    file1.write(code)
    file1.close()
    return "done!"

if __name__ == "__main__":
    if len(sys.argv) < 4 :
        print('faltou um argumento')
        sys.exit()
    else:
        m0 = sys.argv[1]
        m1 = sys.argv[2]
        m2 = sys.argv[3]
        print(genCode(m0,m1,m2))
