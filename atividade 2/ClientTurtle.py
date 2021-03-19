import rclpy 
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from turtlesim.srv import TeleportRelative
import colorama 
from colorama import Fore

rclpy.init()
node = Node("turtle_client")
node.get_logger().info("Cliente Iniciado")
cliente = node.create_client(TeleportRelative,"/turtle1/teleport_relative")
while not cliente.wait_for_service(1.0):
    node.get_logger().warn("Esperando o server")

req = TeleportRelative.Request()

req.angular = float(1)
req.linear = float(2)

future = cliente.call_async(req)
rclpy.spin_until_future_complete(node,future)

log = Fore.GREEN+"Angular is: {a} and Linear is: {b}".format(a=str(req.angular),b=str(req.linear))
print(Fore.RESET)

try:
    resposta = future.result()
    node.get_logger().info(log)
except Exception as e :
    node.get_logger().error("Service call failed "+str(e))

rclpy.shutdown() 
