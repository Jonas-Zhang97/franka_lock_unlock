from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():
    #  args that can be set from the command line or a default will be used
    hostname = DeclareLaunchArgument(
        "hostname", default_value="192.168.1.10"
    )
    username = DeclareLaunchArgument(
        "username", default_value="admin"
    )
    password = DeclareLaunchArgument(
        "password", default_value="admin"
    )

    return LaunchDescription([
        Node(
            name="franka_lock_unlock"
            pkg="franka_lock_unlock"
            exec="lock_unlock"
            output="screen"
            
            args="$(var hostname) $(var username) $(var password) -u -l -w -r -p"
        ),
    ])

