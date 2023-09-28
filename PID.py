#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.qos import qos_profile_sensor_data



class MinimalSubscriber(Node):
	def __init__(self):
		super().__init__('scan_demo')
		self.error=[]
		self.scan_sub=self.create_subscription(LaserScan,'scan',self.laser_callback,qos_profile_sensor_data)
		self.publisher_=self.create_publisher(Twist,'cmd_vel',10)
		self.laser_ranges = []
		for i in range(1400):
			self.laser_ranges.append(0.0)
		
		self.cmd=Twist()
		timer_period=1.0
		self.timer=self.create_timer(timer_period,self.timer_callback)
		self.i=0
		self.previous_error=0


	def PID(self):
		self.cmd.linear.x = 0.2
		
		kp = 0.5
		ki = 0.2
		kd = 1.0
		
		dd = 0.5
		md = min(self.laser_ranges[900:1350]) 
		
		print(md)
		
		e = dd - md
		print(e)
		if e > 0.5:
			e =0.5
		if e < -0.5:
			e = -0.5		
		print("=========")
		print(md)	
		self.error.append(e)
		
		print(self.error)
		
		if len(self.error)>9:
			self.error.pop(0)
		
		
		ei = sum(self.error)
		if ei > 0.5:
			ei = 0.5
		if ei < -0.5:
			ei = -0.5	
		ed = e - self.previous_error
		
		print(self.previous_error)
		
		self.previous_error=e
		
		output = (kp * e) + (ki *ei) + (kd * ed)
		
		self.cmd.angular.z = output
		
		
           
	def timer_callback(self):
		self.PID()
		self.publisher_.publish(self.cmd)
		string='Publishing:'+str(self.cmd.linear.x)
		self.get_logger().info(string)
         	
	def laser_callback(self,msg):
		self.get_logger().info(str(msg.ranges[1080]))
		self.laser_ranges=msg.ranges
		
def main(args=None):
	rclpy.init(args=args)
	
	minimal_subscriber=MinimalSubscriber()
	rclpy.spin(minimal_subscriber)
	
	
	
	minimal_publisher.destroy_node()
	rclpy.shutdown()
if __name__=='__main__':
	main()			
		
        	       
