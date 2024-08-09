from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription

from launch_ros.actions import Node

def generate_launch_description():
    cam_info_sub = Node(
        package='depthai_ros_driver',
        executable='RX_simplified.py',
        name='OAK_cam_info_sub',
    )

    # Run the node
    return LaunchDescription([
        cam_info_sub
    ])