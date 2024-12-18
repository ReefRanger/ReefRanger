import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/reefranger/Desktop/ReefRanger/robot/robot/src/install/pathctrl'
