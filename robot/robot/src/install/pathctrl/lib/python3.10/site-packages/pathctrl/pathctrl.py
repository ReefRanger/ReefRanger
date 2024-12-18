import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from move_interface.action import Move


class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._action_client = ActionClient(self, Move, 'navigatetable')
        self.timer = self.create_timer(2.0, self.timer_callback)

        self.state = 'MissionStart'  # Initial state
        self.command = 'gototarget'

    def timer_callback(self):
        if self.state == 'MissionStart':
            if self.command == 'gototarget':
                self.gototarget()
                self.command = 'wait'
            self.get_logger().info(self.state+' '+self.command)

        elif self.state =='MoveToTable':
            self.get_logger().info('State after :)')
  

    def gototarget(self):
        goal_msg = Move.Goal()
        goal_msg.targetx = 1.0
        goal_msg.targety = 1.0

        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.gototarget_init_callback)

    def gototarget_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.success))
        self.state = 'MoveToTable'  # Initial state
        self.get_logger().info('Completed Task Mission Start')

        
    def gototarget_init_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('go target rejected :(')
            return

        self.get_logger().info('started go target')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.gototarget_callback)






def main(args=None):
    rclpy.init(args=args)

    action_client = FibonacciActionClient()

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()